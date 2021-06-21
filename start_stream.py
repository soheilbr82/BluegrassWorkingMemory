import sys

from lib.dummylsl import DummyLSL


def main(argv):
    # if no arguments are provided, default ia to stream 4 channels with fs=250Hz to LSL

    lsl1 = DummyLSL("DummyStream1", 1)
    lsl1.create_lsl()
    lsl1.begin(autostart=True)


# lsl2 = DummyLSL("DummyStream2", 2)
# lsl2.create_lsl()
# lsl2.begin(autostart=True)


if __name__ == '__main__':
    main(sys.argv[1:])
