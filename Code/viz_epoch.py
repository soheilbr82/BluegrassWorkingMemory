import pdb
from pyqtgraph.Qt import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np
import pyqtgraph as pg
from pylsl import StreamInfo, StreamInlet, resolve_byprop

app = QtGui.QApplication([])

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)
pg.setConfigOption('background', 'w')


class EpochViewer(pg.GraphicsWindow):
    def __init__(self, fs_new=128, channels=1):
        super(EpochViewer, self).__init__()
        self.resize(1000, 1800)
        self.fs_new = fs_new
        self.setWindowTitle('Epoch Viewer')
        self.monitor = QDesktopWidget().screenGeometry(0)
        self.move(self.monitor.left(), self.monitor.top())

        self.plots = []

        streams = resolve_byprop("type", "EPOCH", timeout=20)  # Contains information about all available lsl inlets
        if StreamInfo.type(streams[0]) == 'EPOCH':
            self.inlet_epoch = StreamInlet(streams[0])

        self.info = self.inlet_epoch.info()
        ch = self.info.desc().child("channels").child("channel")
        # Check if LSL contains channel labels
        if self.info.desc().child("channels").child("channel").child_value("label"):
            self.channels = []
            for k in range(channels):

                self.channels.append(ch.child_value("label"))
                ch = ch.next_sibling()
        else:
            self.channels = []
            for i in range(0, channels):
                self.channels.append("Channel " + str(i + 1))

        self.x = np.linspace(-0.2, 0.8, self.fs_new)
        self.legend = None
        self.target = True
        self.non_target = True

        self.epochOneAlphas = np.array([0.8, 1, 0.1, 0.2, 0.3])
        self.epochTwoAlphas = np.array([0.8, 1, 0.1, 0.2, 0.3])

        self.epochOneWidth = np.array([3, 5, 0.2, 0.5, 1])
        self.epochTwoWidth = np.array([3, 5, 0.2, 0.5, 1])

        self.linesPlotted = False
        self.epochOne = [[0 for i in range(5)] for c in range(len(self.channels))]
        self.epochTwo = [[0 for i in range(5)] for c in range(len(self.channels))]
        self.epochOneIndex = 0
        self.epochTwoIndex = 0

        self.ci.layout.setColumnMaximumWidth(0, 700)
        self.ci.layout.setColumnMaximumWidth(1, 700)
        for i in range(len(self.channels)):
            p = self.addPlot(title="%s" % self.channels[i], rowspan=1)
            # p.setYRange(-2, 2)
            self.plots.append(p)

            # p.addLegend()
            if i == 0:
                l = pg.LegendItem((10, 10), offset=(-10, 10))
                l.setParentItem(p.graphicsItem())
                self.legend = l

            p.enableAutoRange(axis=pg.ViewBox.YAxis, enable=True)
            # p.enableAutoRange(x=False, y=True)
            if i % 2:
                self.nextRow()
        self.createTimer()

    def createTimer(self):
        self.main_timer = QTimer()
        self.main_timer.timeout.connect(self.main_loop)
        self.main_timer.start(30)

    def main_loop(self):
        try:
            chunk, timestamp = self.inlet_epoch.pull_chunk(timeout=0.01)

        except IOError:
            pass

        if len(chunk) > 0:
            chunk = np.asarray(chunk)
            lineChange = []

            if self.epochOne[0].count(0) == 0:
                for c in range(len(self.channels)):
                    if chunk[-1][0] == 1:
                        lineOne = self.epochOne[c][self.epochOneIndex]
                        self.plots[c].removeItem(lineOne)

            if self.epochTwo[0].count(0) == 0:
                for c in range(len(self.channels)):
                    if chunk[-1][0] == -1:
                        lineTwo = self.epochTwo[c][self.epochTwoIndex]
                        self.plots[c].removeItem(lineTwo)

            for c in range(len(self.channels)):
                if chunk[-1][0] == 1:
                    p = self.plots[c].plot(x=self.x, y=chunk[c, :], clear=False,
                                           pen=pg.functions.mkPen([255, 0, 0], width=5), name="Target")
                    self.epochOne[c][self.epochOneIndex] = p

                    if self.target:
                        self.legend.addItem(p, 'Target')
                        self.target = False

                elif chunk[-1][0] == -1:
                    p = self.plots[c].plot(x=self.x, y=chunk[c, :], clear=False,
                                           pen=pg.functions.mkPen([0, 0, 255], width=5), name="Non-Target")
                    self.epochTwo[c][self.epochTwoIndex] = p

                    if self.non_target:
                        self.legend.addItem(p, 'Non-Target')
                        self.non_target = False

            if chunk[-1][0] == 1:
                lineChange = [x for x in range((5 - self.epochOne[0].count(0)))]
            elif chunk[-1][0] == -1:
                lineChange = [x for x in range((5 - self.epochTwo[0].count(0)))]

            if self.linesPlotted:
                for i in range(len(lineChange)):
                    for c in range(len(self.channels)):
                        if chunk[-1][0] == 1:
                            lineOne = self.epochOne[c][lineChange[i]]
                            lineOne.setAlpha(self.epochOneAlphas[i], False)
                            lineOne.setPen(pg.functions.mkPen([255, 0, 0], width=self.epochOneWidth[i]))

                        elif chunk[-1][0] == -1:
                            lineTwo = self.epochTwo[c][lineChange[i]]
                            lineTwo.setAlpha(self.epochTwoAlphas[i], False)
                            lineTwo.setPen(pg.functions.mkPen([0, 0, 255], width=self.epochTwoWidth[i]))

                if chunk[-1][0] == 1:
                    self.epochOneAlphas = np.roll(self.epochOneAlphas, 1)
                    self.epochOneWidth = np.roll(self.epochOneWidth, 1)
                elif chunk[-1][0] == -1:
                    self.epochTwoAlphas = np.roll(self.epochTwoAlphas, 1)
                    self.epochTwoWidth = np.roll(self.epochTwoWidth, 1)

            else:
                self.linesPlotted = True

            if chunk[-1][0] == 1:
                if self.epochOneIndex < 4:
                    self.epochOneIndex += 1
                else:
                    self.epochOneIndex = 0
            elif chunk[-1][0] == -1:
                if self.epochTwoIndex < 4:
                    self.epochTwoIndex += 1
                else:
                    self.epochTwoIndex = 0


# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        if len(sys.argv) > 2:
            o = EpochViewer(fs_new=int(sys.argv[1]), channels=int(sys.argv[2]))
        else:
            o = EpochViewer()
        sa = pg.QtGui.QScrollArea()
        sa.setWidget(o)
        o.show()
        sa.show()
        QtGui.QApplication.instance().exec_()
        sys.exit(1)
