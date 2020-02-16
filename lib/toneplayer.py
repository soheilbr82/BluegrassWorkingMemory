from psychopy.preferences import Preferences

prefs = Preferences()
prefs.hardware['audioLib'] = ['PTB']
from psychopy.sound.backend_ptb import SoundPTB

duration = 0.05
volume = 0.5


class toneplayer:
    def __init__(self):
        self.sound_1 = SoundPTB('A', secs=duration, volume=volume, stereo=True, hamming=True, name='sound_1')
        self.sound_2 = SoundPTB('B', secs=duration, volume=volume, stereo=True, hamming=True, name='sound_2')

    def correct(self):
        self.sound_1.play()

    def incorrect(self):
        self.sound_2.play()

    def stop(self):
        self.sound_1.stop(reset=True, log=False)
        self.sound_2.stop(reset=True, log=False)

