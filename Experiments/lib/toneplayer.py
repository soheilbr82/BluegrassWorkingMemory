from psychopy.sound.backend_pygame import SoundPygame

duration = 0.2
volume = 0.5

class toneplayer:
    def __init__(self):
        # self.sound_1 = SoundPTB('A', secs=duration, volume=volume, stereo=True, hamming=True, name='sound_1')
        # self.sound_2 = SoundPTB('B', secs=duration, volume=volume, stereo=True, hamming=True, name='sound_2')

        Pos = './lib/sound/bird.wav'
        Neg = './lib/sound/bang.wav'
        self.sound_1 = SoundPygame(Pos, secs=duration, stereo=True, hamming=True, name='sound_1')
        self.sound_2 = SoundPygame(Neg, secs=duration, stereo=True, hamming=True, name='sound_2')

    def correct(self):
        self.sound_1.play()

    def incorrect(self):
        self.sound_2.play()

    def stop(self):
        self.sound_1.stop()
        self.sound_2.stop()
