#!/usr/bin/python
# -*- coding: cp1251 -*-

"""

    A threaded implementation of the "egi.netstation" component .

    (This variant of the threaded implementation is a bit more complicated,
      and a bit more messy -- but may be easier to support, as the method names
      from the " internal EGI.Netstation class " are wrapped automatically
      in the local Netstation wrapper class definition . )


"""

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

import simple as internal # Netstation object, mostly
from socket_wrapper import Socket

#
# "forward" these names to be used from outside
#

Error = internal.EgiError
ms_localtime = internal.ms_localtime

#
# the name(s) to be used internally
#

## _Netstation = internal.Netstation

import types # MethodType, FunctionType
## import inspect # .ismethod()
from StringIO import StringIO

# -----------------------------------------------------------------------------

from threading import Thread
from Queue import Queue

import time # time() for 'soft timeouts'

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

#
# an internal helper class -- a very thin wrapper around 'a message' between two threads
#
class _Command:
    """
        a command is simply the name of the method to call --
        -- and a dictionary with the argument name / value pairs

    """

    #
    # there are three things to implement: (1) pack op., (2) unpack op., (3) helper methods .
    #

    # (1) " packing ":

    def __init__(self, method_name, kwargs = None):

        if kwargs is None:  kwargs = {}

        self._func_name = method_name
        self._kwargs = kwargs

    # (2) " unpacking ":

    def name(self):
        """ returns the name of the function (method, actually) to call """

        return self._func_name

    def kwargs(self):
        """ returns the key/value set of the arguments to pass to the function (ugh, "to the method", I wanted to say) """

        return self._kwargs

    # (3) " helper method ":

    @staticmethod
    def call(obj, attrname, kwargs):
        """ call the given method with the arguments specified """

        '''
        bound = getattr(obj, attrname, None)
        if bound is not None:
            # assert callable(bound)

            return bound(**kwargs)

        # else return None
        '''

        # it is better not to eat exceptions here

        bound = getattr(obj, attrname)
        return bound(**kwargs)


    def invoke(self, obj):
        """ invoke the 'attrname' with 'kwargs' (both stored here) on the object 'obj' """

        return self.call(obj, self.name(), self.kwargs())




# -----------------------------------------------------------------------------

class _NetstationThread(Thread):

    """ Class implementing the thread instance that be sending the messages """

    def __init__(self, to_send, received):
        """
            the thread will send the strings from the 'to_send' queue,
            read the response with the read functions packed together with the strings to send,
            put the result in the 'received' queue
        """

        Thread.__init__(self)

        self.setName("Netstation Thread") # =%:-)

        self._netstation_object      =  internal.Netstation()

        self._to_send   =  to_send
        self._received  =  received

    ## -----------------------------------------------------------

    @staticmethod
    def is_end_marker(packet):
        """ is this enry from the queue an end marker ? """

        return (packet is None)


    def _process(self, packet):
        """ pass the received information to internal 'netstation' object to make a method call """

        return packet.invoke(self._netstation_object)


    ## -----------------------------------------------------------

    def run(self):

        # # debug
        # print self.getName(), ":  start "

        while True:

            packet = self._to_send.get()

            if self.is_end_marker(packet):

                # # debug
                # print self.getName(), ":  we're done ! "

                # we are assuming that the 'None' "packet" is an absolute "end marker" --
                # -- so it is safe to disconnect now
                self._disconnect()

                break

            #
            # we could change the packet format and add some timestamps and/or packet numbers ...
            #

            ret = self._process(packet)

            self._received.put(ret) # also could have added the input timestamp, output timestamp and the packet number


        # # debug
        # print self.getName(), ":  closing() "

    ## -----------------------------------------------------------

    #
    # let's call the 'self._netstation_object.connect()' method directly
    #

    def connect(self, str_address, port_no):
        """ "forward" this method to the inner 'netstation' object """

        return self._netstation_object.connect(str_address, port_no)


    def _disconnect(self):
        """ this method is intended to be called internally and automatically) """

        return self._netstation_object.disconnect()



# -----------------------------------------------------------------------------

#
# the simplest version without "packet stamping" and "back synchronization" (needed for good sync()-ing)
#

#
# TODOtodo: (a) wrap the process of starting of the new thread (and finalization) in separate functions ;
#           (b) re-use (a) ;
#           (c) syncronize in single-threaded mode .
#

class Netstation:

    """ Provides Python interface for a connection with the Netstation via a TCP/IP socket. """

    ## -----------------------------------------------------------

    def __init__(self):

        self._to_send = Queue()
        self._to_receive = Queue()

        self._netstation_thread = _NetstationThread(self._to_send, self._to_receive)

    ## -----------------------------------------------------------

    def _put(self, data):
        """ a shortcut to put sth in the 'to-send' queue """

        self._to_send.put(data)

        # return None

    def _get(self):
        """ a shortcut to get sth from the 'to-receive' queue ; nb.: blocks ! """

        data = self._to_receive.get()
        return data

    ## -----------------------------------------------------------

    def enumerate_responses(self):
        """ (1) check .qsize() ; (2) .get() all these elements """

        n_available = self._to_receive.qsize()

        for i in xrange(n_available):

            data = self._get()
            yield data

        # ''' return None '''

    ## # a shortcut to be exported
    ## enumerate_responses = _enumerate_received


    # a simple 'dummy processor' made for convenience
    ## def process_responses(self, resp_handler = lambda resp: pass):
    def process_responses(self):

        for resp in self.enumerate_responses():

            # resp_handler(resp)
            pass

        # return None

        ## change the return value depending on the resp_handler() return result ?
        ## (e.g. break the loop on True ?)

        # don't need all these complifications at the moment)

    ## -----------------------------------------------------------


    def _ns_thread_is_running(self):
        """ returns True if our 'postman' thread is stil busy with doing something """

        return self._netstation_thread.isAlive()

    ## -----------------------------------------------------------

    '''

    def _connect(self, str_address, port_no):
        """ connect to the Netstaton machine """

        self._socket.connect(str_address, port_no)

        # return None

    def _disconnect(self):
        """ close the connection """

        self._socket.disconnect()

        # return None

    '''


    ## -----------------------------------------------------------

    def initialize(self, str_address, port_no):
        """ open the socket /and/ start the 'Mr. Postman' thread """

        ## # this could be in __init__() as well

        self._netstation_thread.connect(str_address, port_no)

        self._netstation_thread.start() # starting thread

        # return None

    def finalize(self, seconds_timeout = 2):
        """ send the thread the 'Done' message and wait until it finishes """

        self._put(None)

        t_start = time.time()

        # if the timeout termination will be of real use,
        # we'll probably want to handle the exception in the 'postman' thread
        while (time.time() - t_start) < seconds_timeout:

            self.process_responses()

        # debug
        print " egi: stopping ... "

        ## self._disconnect()

        # del self._to_send
        # del self._to_receive

        # del _netstation_thread

    ## -----------------------------------------------------------
    ## -----------------------------------------------------------

    #
    # may be at some moment we should replace the repetitive code below
    # to a getattr()-based code (alternatives: (a) "on-the-fly patching",
    # (b) metaclasses, (c) exec statement and may be more ;)
    #
    # (a) "static is better than dynamic" in the terms of execution cost ;
    # (b) "simple is better than complex")
    # (c) "explicit is better than implicit" -- i.e. "it is better to have clear syntax highlighting"
    #
    # // finally preferred the exec way for the sake of easy ipython usage)

    # don't pollute the namespace too much
    local_names = locals().keys()

    from fwhelper import FunctionWrappingHelper as FWH

    # a shortcut
    _NS = internal.Netstation

    ## for name, value in _Netstation.__dict__.iteritems():
    for name in _NS.__dict__.iterkeys():

        value = getattr(_NS, name)

        ## # debug
        ## print name, value, type(value), \
        ##       callable(value), isinstance(value, (types.FunctionType, types.MethodType)), \
        ##       inspect.ismethod(value)

        if name.startswith('_'): continue
        '''
        if type(value) is not types.FunctionType \
        and type(value) is not types.St: continue
        '''
        ## if not isinstance(value, (types.FunctionType, types.MethodType)): continue
        if not callable(value): continue

        # do not want to replace any of the existing names
        ## could actually have "forwarded" names from a predefined list

        if name in local_names: continue

        #
        # simple form of what we want to simulate goes below
        #

        '''
        def BeginSession(self):
            """ say 'hi!' to the server """

            packet = _Command('BeginSession')
            # return self._process(packet)
            self._put(packet)

        '''

        #
        # a more complicated xample of the internal code:
        #

        '''

        kwargs = {                             \
                   'key'        : key         ,
                   'timestamp'  : timestamp   ,
                   'label'      : label       ,
                   'description': description ,
                   'table'      : table       ,
                   'pad'        : pad         \
                }

        packet = _Command('send_event', kwargs)
        self._put(packet)

        '''

        # else: ## start generating the call

        fwh = FWH(value)

        #
        # the declaration
        #

        header = StringIO()
        header.write('def %s(' % (name,))
        for entry in fwh.enum_argentries(b_all = True):

            ## if entry == 'self': continue
            header.write('%s, ' % (entry,))


        header.write('):\n')
        # "a bit of pretty-printing"
        header.write('\n')

        header = header.getvalue()

        #
        # the helpstring
        #

        helpstr = getattr(value, '__doc__', None)

        #
        # the call
        #

        call = StringIO()

        # put the helpstring
        if helpstr: call.write('"""%s"""\n\n' % (helpstr,))

        if fwh.nargs() > 1:  # do we have "non-self" arguments ?

            call.write('kwargs = {')
            # at the moment we do not pass 'kwargs through kwargs' (" { ... , '*kwargs': kwargs } " ? kwargs_old.update(kwargs_new) ? )
            for entry in fwh.enum_argentries(b_no_default_values = True, b_all = False):

                if entry == 'self': continue
                call.write("'%s': %s, " % (entry, entry))

            call.write(' }\n')

            # "a bit of pretty-printing"
            call.write('\n')

            call.write("packet = _Command('%s', kwargs)\n" % (name))

        else:  # no non-trivial arguments present

            call.write("packet = _Command('%s')\n" % (name))

        call.write("self._put(packet) \n")
        # "a bit of pretty-printing"
        call.write('\n')

        call.seek(0)

        # indent

        call_ = StringIO()
        for line in call.readlines():
            call_.write('\t' + line)
        call_.write('\n')

        call_ = call_.getvalue()

        code = header + call_
        exec code

        ## # debug
        ## print code

        # clean things
        # # probably should check locals(), add the name-s, then clean all the rest

        ## del code, line, call_, call, entry, header, fwh, value, name
        ## del code, line, call_, call, header ## fwh, value, name

        local_names.append(name)

    # del code, line, call_, call, entry, header, fwh, value, name
    extended_ = locals().keys()
    # here 'v' stands for "var", not for "vendetta"
    delete_ = [ v for v in extended_ if v not in local_names ]
    for v in delete_: exec "del %s" % (v,)
    del delete_, v


    '''
    ## -----------------------------------------------------------


    def BeginSession(self):
        """ say 'hi!' to the server """

        packet = _Command('BeginSession')
        # return self._process(packet)
        self._put(packet)


    def EndSession(self):
        """ say 'bye' to the server """

        packet = _Command('EndSession')
        self._put(packet)


    ## -----------------------------------------------------------

    def StartRecording(self):
        """ start recording to the selected (externally) file """

        packet = _Command('StartRecording')
        self._put(packet)


    def StopRecording(self):
        """ stop recording to the selected file;
            the recording can be resumed with the BeginRecording() command
            if the session is not closed yet .
        """

        packet = _Command('StopRecording')
        self._put(packet)

    ## -----------------------------------------------------------

    #
    # the next two are not supposed to be used "manually" (by the user) --
    # -- especially becuase at least our version of the Netstation software
    # often crashes if the delay between the 'attention' and the 'time' commands
    # exceeds some dark secretly defined timeout value
    #

    def _SendAttentionCommand(self):
        """ Sends and 'Attention' command """ # also pauses the recording ?

        packet = _Command('SendAttentionCommand')
        self._put(packet)


    def _SendLocalTime(self, ms_time = None):
        """ Send the local time (in ms) to Netstation; usually this happens after an 'Attention' command """

        packet = _Command('SendAttentionCommand', { 'ms_time': ms_time })
        self._put(packet)

    ## -----------------------------------------------------------

    def sync(self, timestamp = None):
        """ a shortcut for sending the 'attention' command and the time info """

        # in the simplest form ,
        # we just send the instructions (and hope they won't be delayed too much) ;
        # though it might be a good idea to wait for the reponse here

        ## self.SendAttentionCommand()
        ## self.SendLocalTime(timestamp)

        # TODO/todo: change the code so that we'll wait for the result in the calling thread

        packet = _Command('sync', { 'timestamp': timestamp })
        self._put(packet)

    ## -----------------------------------------------------------

    # send_event, send_simple_event

    def send_event(self, key, timestamp = None, label = None, description = None, table = None, pad = False):
        """
            Send an event ; note that before sending any events a sync() has to be called
            to make the sent events effective .

            Arguments:
            -- 'id' -- a four-character identifier of the event ;
            -- 'timestamp' -- the local time when event has happened, in milliseconds ;
                              note that the "clock" used to produce the timestamp should be the same
                              as for the sync() method, and, ideally,
                              should be obtained via a call to the same function ;
                              if 'timestamp' is None, a time.time() wrapper is used .
            -- 'label' -- a string with any additional information, up to 256 characters .
            -- 'description' -- more additional information can go here (same limit applies) .
            -- 'table' -- a standart Python dictionary, where keys are 4-byte identifiers,
                          not more than 256 in total ;
                          there are no special conditions on the values,
                          but the size of every value entry in bytes should not exceed 2 ^ 16 .

            Note A: due to peculiarity of the implementation, our particular version of NetStation
                    was not able to record more than 2^15 events per session .

            Note B: it is *strongly* recommended to send as less data as possible .

        """


        kwargs = {                             \
                   'key'        : key         ,
                   'timestamp'  : timestamp   ,
                   'label'      : label       ,
                   'description': description ,
                   'table'      : table       ,
                   'pad'        : pad         \
                }

        packet = _Command('send_event', kwargs)
        self._put(packet)


    ## -----------------------------------------------------------

    '''


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    print __doc__
    print "\n === \n"
    # print "module dir() listing: ", __dict__.keys()
    print "module dir() listing: ", dir()


