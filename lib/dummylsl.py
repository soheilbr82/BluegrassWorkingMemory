'''
  dummylsl.py
  ---------------

  This module generates a simulated LSL instances using default parameters into labstreaminglayer


'''

import sys
import threading
import time

import numpy as np
from pylsl import StreamInfo, StreamOutlet, local_clock


class DummyLSL:
    IDLE = 1
    STREAMING = 2
    STOPPING = 3

    def __init__(self, name, idNum):
        print("\n-------INSTANTIATING DUMMY BOARD-------")
        self.n_channels = 18
        self.sample_freq = 128
        self.name = name
        self.id = idNum
        self.state = self.IDLE

        self.stream_info = StreamInfo(self.name, "EEG", self.n_channels, self.sample_freq, 'float32',
                                      "dummy_eeg_id%s" % str(self.id))
        self.outlet = StreamOutlet(self.stream_info)

    def create_lsl(self):
        info_args = dict(
            name=self.name,
            type="EEG",
            channel_count=self.n_channels,
            nominal_srate=self.sample_freq,
            channel_format="float32",
            source_id="dummy_eeg_id%s" % self.id
        )

        self.stream_info = StreamInfo(**info_args)

        # channel locations
        chns = self.stream_info.desc().append_child('channels')
        if self.n_channels == 16:
            labels = ['Fp1', 'Fp2', 'C3', 'C4', 'T5', 'T6', 'O1', 'O2', 'F7', 'F8', 'F3', 'F4', 'T3', 'T4', 'P3', 'P4']
        elif self.n_channels == 8:
            labels = ['Fp1', 'Fp2', 'C3', 'C4', 'T5', 'T6', 'O1', 'O2']
        elif self.n_channels == 4:
            labels = ['C3', 'C4', 'P3', 'P4']
        else:
            labels = []

        for label in labels:
            ch = chns.append_child("channel")
            ch.append_child_value('label', label)
            ch.append_child_value('unit', 'microvolts')
            ch.append_child_value('type', 'EEG')

        # additional Meta Data
        self.stream_info.desc().append_child_value('manufacturer', 'OpenBCI Inc.')

        # create StreamOutlet
        self.outlet = StreamOutlet(self.stream_info)

        print("--------------------------------------\n" +
              "LSL Configuration: \n" +
              "  Stream %s: \n" % str(self.id)+
              "      Name: " + info_args["name"] + " \n" +
              "      Type: " + info_args["type"] + " \n" +
              "      Channel Count: " + str(self.n_channels) + "\n" +
              "      Sampling Rate: " + str(self.sample_freq) + "\n" +
              "      Channel Format: " + info_args["channel_format"] + " \n" +
              "      Source Id: " + info_args["source_id"] + " \n" +
              "Electrode Location Montage:\n" +
              str(labels) + "\n" +
              "---------------------------------------\n")

    def cleanUp(self):
        print("Cleaned up")

    def build_sample(self, t):
        n_signal_components = 3

        amplitudes = .1 + .2 * np.random.rand(self.n_channels, n_signal_components).astype(
            np.float32) / n_signal_components
        offsets = 2 * np.pi * np.random.rand(self.n_channels, n_signal_components).astype(np.float32)

        res = np.empty(self.n_channels)
        for i in range(self.n_channels):
            res[i] = np.sum([a * np.sin(t + o) for a in amplitudes[i] for o in offsets[i]])
        return res

    def start_streaming(self):
        def dummy_stream():

            t = local_clock()

            while self.state != self.STOPPING:
                if local_clock() - t >= 1 / self.sample_freq:
                    sample = self.build_sample(t)
                    self.outlet.push_sample(sample, t)

                    t = local_clock()

        self.state = self.STREAMING
        stream_thread = threading.Thread(target=dummy_stream)
        stream_thread.daemon = True
        stream_thread.start()

        print("Current streaming: {} EEG channels at {} Hz\n".format(self.n_channels, self.sample_freq))

    def stop_streaming(self):
        self.state = self.STOPPING
        print("Streaming stopped.\n")

    def begin(self, autostart=False):
        print("--------------INFO---------------")
        print(
            "Commands: \n" + \
            "    Type \"/start\" to stream to LSL \n" + \
            "    Type \"/stop\" to stop stream.\n" + \
            "    Type \"/exit\" to disconnect the board. \n" + \
            "Advanced command map available at http://docs.openbci.com")

        print("\n-------------BEGIN---------------")
        # Init board state
        # s: stop board streaming; v: soft reset of the 32-bit board (no effect with 8bit board)

        s = 'sv'

        if autostart:
            s = "/start"

        while s != "/exit":
            # Send char and wait for registers to set
            if not s:
                pass
            elif self.state == self.STREAMING and s != "/stop":
                print(
                    "Error: the board is currently streaming data, please type '/stop' before issuing new commands.")
            else:
                # read silently incoming packet if set (used when stream is stopped)
                flush = False

                if '/' == s[0]:
                    s = s[1:]
                    rec = False  # current command is recognized or fot

                    if "start" in s:
                        self.start_streaming()
                        rec = True
                    elif 'stop' in s:
                        self.stop_streaming()
                        rec = True
                        flush = True
                    elif 'loc' in s:
                        self.change_locations(s[4:])
                        rec = True
                        flush = True
                    if rec is False:
                        print("Command not recognized...")

                if not flush:
                    print('')

            # Take user input
            # s = input('--> ')
            if sys.hexversion > 0x03000000:
                s = input('--> ')
            else:
                s = input('--> ')

    def change_locations(self, locs):
        new_locs = [loc for loc in locs.split(',')]

        chns = self.stream_info.desc().child('channels')
        ch = chns.child("channel")
        for label in new_locs:
            ch.set_child_value('label', label)
            ch = ch.next_sibling()

        print("New Channel Montage:")
        print(str(new_locs))

        # create StreamOutlet
        self.outlet = StreamOutlet(self.stream_info)
