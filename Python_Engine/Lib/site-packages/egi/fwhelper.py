

# standard
from __future__ import print_function, division
import inspect
import types


# A helper to generate wrapping code for a function -- to be used with
# exec statement.

class Undefined(object):
    """ Need some placeholder as a special alternative to 'None' """
    ## pass


def infinite_pad(iterable, pad_value):
    """
    An iterator that returns the 'pad_value' after the end of the
    sequence.
    """

    for elem in iterable:
        yield elem

    while True:  # or: while limit != 0 # so negative value will give same 'infinity' effect
        yield pad_value


class FunctionWrappingHelper(object):

    """ loads function info with inspect, and then provides some convenient shortcuts """

    def __init__(self, fn):

        # nb: for py 2.5 , 'method.func_code.co_varnames' is 'method.im_func.func_code.co_varnames' (!)
        if isinstance(fn, types.MethodType):
            fn = fn.im_func

        args, varargs, keywords, defaults = inspect.getargspec(fn)
        self._args = args
        self._varargs = varargs
        self._keywords = keywords
        self._defaults = defaults
        self._func_name = fn.func_name

    @property
    def name(self):
        return self._func_name

    @property
    def argnames(self):
        return self._args

    @property
    def vargs_name(self):
        return self._varargs

    @property
    def kwargs_name(self):
        return self._keywords

    @property
    def defaults(self):
        return self._defaults

    def nargs(self):
        return len(self.argnames)

    def enum_argentries(self, b_no_default_values = False, b_all = False):
        """ for f(a, b = 1, *v, *d) returns 'a', 'b=1', [ '*v', '**d' ] -- the last ones for b_all == True """

        # " zip things "

        rnames = []
        rvalues = []

        if self.argnames is not None:
            rnames = list(self.argnames)
        if self.defaults is not None:
            rvalues = list(self.defaults)

        rnames.reverse()
        rvalues.reverse()

        # rnames.reverse()
        # rvalues.reverse()

        # pairs = map(None, rnames, rvalues)

        pairs = zip(rnames, infinite_pad(rvalues, Undefined))

        pairs.reverse()

        # now iterate through things

        for name, value in pairs:

            ## yield "%s=%s" % (name, repr(value))

            ## '''

            ## if (not b_no_default_values) and (value is not None):
            ## if value is not Undefined:
            if (not b_no_default_values) and (value is not Undefined):

                yield "%s=%s" % (name, repr(value))

            else:

                yield name

            ## '''

        if b_all:

            if self.vargs_name is not None:

                yield '*%s' % self.vargs_name

            if self.kwargs_name is not None:

                yield '**%s' % self.kwargs_name



    def dump(self):
        """ [debug] dump the function info to stdout """

        print '\n\n---\n\n', self.name, ':'
        for entry in self.enum_argentries(True):

            print '\t', entry, ','


if __name__ == "__main__":

    print __doc__
    print "\n === \n"
    # print "module dir() listing: ", __dict__.keys()
    print "module dir() listing: ", dir()

    def test_fn0(): pass
    def test_fn1(arg): print arg # just to have sth different
    def test_fn2(a,b,c): pass
    def test_fn3(a,b,c,d=1,e="abc foods", *args): pass
    def test_fn4(a,b,c,*args, **kwargs): pass
    def test_fn5(a,b,c,d,e=1, f=1.0, g=[1,2,3], h = (1,2,3), i = "abc def", j = lambda x: x, k = FunctionWrappingHelper(lambda x: x), *args, **kwargs):
        print a,b,c,d,e,f,g,h,i,j,k
        print "args: ", args
        print "kwargs: ", kwargs
        return a

    def test_fn6(a = None): pass


    for f in [test_fn0, test_fn1, test_fn2, test_fn3, test_fn4, test_fn5, test_fn6 ]:
        w = FunctionWrappingHelper(f)
        print '\n\n---\n\n', w.name, ':'
        for entry in w.enum_argentries(b_all = True):
            print '\t', entry, ','







