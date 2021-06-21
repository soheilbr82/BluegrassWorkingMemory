#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on June 05, 2021, at 11:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)


# Store info about the experiment session
if len(sys.argv) > 1:
    ss = ' '.join([x for x in sys.argv[1:]])
    expInfo = eval(ss)
    # expInfo = {i.split(': ')[0]: i.split(': ')[1] for i in ss.split(', ')}
    expName = 'STM'

else:
    expName = 'STM'
    expInfo = {'Participant ID': '', 'Age': '', 'Sex': ['Male', 'Female'],
                        'Handedness': ['Right-handed', 'Left-handed', 'Ambidextrous'],
                        'EEG headset': ['Emotiv EPOC(+)', 'gtec Unicorn', 'gtec Nautilus 32'],
                        'Experiment Mode': ['intro', 'Resting_Eyes_Opened', 'Resting_Eyes_Closed',
                                            'train', 'neurofeedback'], 'Visualize Epochs': False,
                        'date': [data.getDateStr()]}
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Participant ID'], expInfo['Experiment Mode'], expInfo['date'])
#filename = 'test'

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Projects\\BluegrassSTM_1.8_WithoutAudiovisual_Win64\\Experiments\\STM_Train_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "initiation"
initiationClock = core.Clock()

# Initialize components for Routine "description_A1_1"
description_A1_1Clock = core.Clock()
polygon_1 = visual.Rect(
    win=win, name='polygon_1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText_1 = visual.TextStim(win=win, name='descriptionText_1',
    text='Round 1\n\nPlease determine whether each image matches one of the images shown with a green border. \n\n press the L key to choose match, and press the A key to choose “non match”.\n\nKeep your left and right pointer fingers on the A and L at all time\n\n\nPress SPACEBAR to continue',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyPressRun_1 = keyboard.Keyboard()

# Initialize components for Routine "Fixation10"
Fixation10Clock = core.Clock()
fixation10 = visual.Rect(
    win=win, name='fixation10',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixationImage10 = visual.ImageStim(
    win=win,
    name='fixationImage10', 
    image='./stimuli/images/fix.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='3 . . .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='2 . .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='1 .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Procedure1"
Procedure1Clock = core.Clock()
blackProc = visual.Rect(
    win=win, name='blackProc',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
greenProc = visual.Rect(
    win=win, name='greenProc',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
ProcTarget = visual.ImageStim(
    win=win,
    name='ProcTarget', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ProcPicture = visual.ImageStim(
    win=win,
    name='ProcPicture', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "waitInterTrial"
waitInterTrialClock = core.Clock()
blackWaitInterTrial = visual.Rect(
    win=win, name='blackWaitInterTrial',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
whiteWaitInterTrial = visual.ImageStim(
    win=win,
    name='whiteWaitInterTrial', 
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "TrialList"
TrialListClock = core.Clock()
blackTrial = visual.Rect(
    win=win, name='blackTrial',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
whiteTrial = visual.Rect(
    win=win, name='whiteTrial',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
TrialPicture = visual.ImageStim(
    win=win,
    name='TrialPicture', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
keyPressTrial_1 = keyboard.Keyboard()
green_1 = visual.ShapeStim(
    win=win, name='green_1', vertices='star7',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
red_1 = visual.Rect(
    win=win, name='red_1',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1.0, depth=-7.0, interpolate=True)

# Initialize components for Routine "Feedback_1"
Feedback_1Clock = core.Clock()

# Initialize components for Routine "InterTrial"
InterTrialClock = core.Clock()
blackWaitInterTrial_2 = visual.Rect(
    win=win, name='blackWaitInterTrial_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
whiteWaitInterTrial_2 = visual.ImageStim(
    win=win,
    name='whiteWaitInterTrial_2', 
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
green_fb_1 = visual.ShapeStim(
    win=win, name='green_fb_1',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
red_fb_1 = visual.Rect(
    win=win, name='red_fb_1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
keyPressTrial_3 = keyboard.Keyboard()
green_3 = visual.ShapeStim(
    win=win, name='green_3', vertices='star7',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
red_3 = visual.Rect(
    win=win, name='red_3',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1.0, depth=-7.0, interpolate=True)

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
fixation = visual.Rect(
    win=win, name='fixation',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixationImage = visual.ImageStim(
    win=win,
    name='fixationImage', 
    image='./stimuli/images/fix.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "end"
endClock = core.Clock()
polygon_end = visual.Rect(
    win=win, name='polygon_end',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
end_text = visual.TextStim(win=win, name='end_text',
    text='That completes Round 1 of the task',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "initiation_2"
initiation_2Clock = core.Clock()

# Initialize components for Routine "description_A2_1"
description_A2_1Clock = core.Clock()
polygon_15 = visual.Rect(
    win=win, name='polygon_15',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText_15 = visual.TextStim(win=win, name='descriptionText_15',
    text='Round 2\n\nNow, you will complete the task again, \nbut this time, you will switch the buttons for “match” and\n “no match\n press the A key to choose match, and press the L key to choose “non match”.\n\nKeep your left and right pointer fingers on the A and L at all time\n\n\nPress SPACEBAR to continue\n\n',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyPressRun_15 = keyboard.Keyboard()

# Initialize components for Routine "Fixation10"
Fixation10Clock = core.Clock()
fixation10 = visual.Rect(
    win=win, name='fixation10',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixationImage10 = visual.ImageStim(
    win=win,
    name='fixationImage10', 
    image='./stimuli/images/fix.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='3 . . .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='2 . .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='1 .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Procedure1_2"
Procedure1_2Clock = core.Clock()
blackProc_2 = visual.Rect(
    win=win, name='blackProc_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
greenProc_2 = visual.Rect(
    win=win, name='greenProc_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
ProcTarget_2 = visual.ImageStim(
    win=win,
    name='ProcTarget_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ProcPicture_2 = visual.ImageStim(
    win=win,
    name='ProcPicture_2', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "waitInterTrial_2"
waitInterTrial_2Clock = core.Clock()
blackWaitInterTrial_3 = visual.Rect(
    win=win, name='blackWaitInterTrial_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
whiteWaitInterTrial_3 = visual.ImageStim(
    win=win,
    name='whiteWaitInterTrial_3', 
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "TrialList_2"
TrialList_2Clock = core.Clock()
blackTrial_2 = visual.Rect(
    win=win, name='blackTrial_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
whiteTrial_2 = visual.Rect(
    win=win, name='whiteTrial_2',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
TrialPicture_2 = visual.ImageStim(
    win=win,
    name='TrialPicture_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
keyPressTrial_2 = keyboard.Keyboard()
green_2 = visual.ShapeStim(
    win=win, name='green_2', vertices='star7',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
red_2 = visual.Rect(
    win=win, name='red_2',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1.0, depth=-7.0, interpolate=True)

# Initialize components for Routine "Feedback_2"
Feedback_2Clock = core.Clock()

# Initialize components for Routine "InterTrial_2"
InterTrial_2Clock = core.Clock()
blackWaitInterTrial_4 = visual.Rect(
    win=win, name='blackWaitInterTrial_4',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
whiteWaitInterTrial_4 = visual.ImageStim(
    win=win,
    name='whiteWaitInterTrial_4', 
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
green_fb_2 = visual.ShapeStim(
    win=win, name='green_fb_2',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
red_fb_2 = visual.Rect(
    win=win, name='red_fb_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
keyPressTrial_4 = keyboard.Keyboard()
green_4 = visual.ShapeStim(
    win=win, name='green_4', vertices='star7',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
red_4 = visual.Rect(
    win=win, name='red_4',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1.0, depth=-7.0, interpolate=True)

# Initialize components for Routine "Fixation_2"
Fixation_2Clock = core.Clock()
fixation_2 = visual.Rect(
    win=win, name='fixation_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixationImage_2 = visual.ImageStim(
    win=win,
    name='fixationImage_2', 
    image='./stimuli/images/fix.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "end_2"
end_2Clock = core.Clock()
polygon_end_2 = visual.Rect(
    win=win, name='polygon_end_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
end_text_2 = visual.TextStim(win=win, name='end_text_2',
    text='Thank you for your participation!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "initiation"-------
continueRoutine = True
# update component parameters for each repeat
# Add random and excel library
import random, xlrd, os, sys
sys.path.append('./lib/')






# Fix random seed
random.seed()
if expInfo['Experiment Mode'] == 'train-A': 
    # Read stimuli excel file
    if expInfo['Handedness'] in ['Right-handed', 'Ambidextrous']:
        infile = './lib/listA1_Righty.xlsx'
    elif expInfo['Handedness'] in ['Left-handed']:
        infile = './lib/listA1_Lefty.xlsx'
    # Number of stimuli
    numBlocks = 8
    numTrials = 20


elif expInfo['Experiment Mode'] == 'train-B': 
    # Read stimuli excel file
    if expInfo['Handedness'] in ['Right-handed', 'Ambidextrous']:
        infile = './lib/listA3_Righty.xlsx'
    elif expInfo['Handedness'] in ['Left-handed']:
        infile = './lib/listA3_Lefty.xlsx'
    # Number of stimuli
    numBlocks = 8
    numTrials = 20

elif expInfo['Experiment Mode'] == 'train-A(short)': 
    # Read stimuli excel file
    if expInfo['Handedness'] in ['Right-handed', 'Ambidextrous']:
        infile = './lib/listA1_Righty.xlsx'
    elif expInfo['Handedness'] in ['Left-handed']:
        infile = './lib/listA1_Lefty.xlsx'
    # Number of stimuli
    numBlocks = 8
    numTrials = 12


elif expInfo['Experiment Mode'] == 'train-B(short)': 
    # Read stimuli excel file
    if expInfo['Handedness'] in ['Right-handed', 'Ambidextrous']:
        infile = './lib/listA3_Righty.xlsx'
    elif expInfo['Handedness'] in ['Left-handed']:
        infile = './lib/listA3_Lefty.xlsx'
    # Number of stimuli
    numBlocks = 8
    numTrials = 12


pictureSize=(0.75,1)
greenSize=(1.6,1.2)




Jitter = []
Duration = []
ISI = []
Picture = []
correctseth = []
Target = []
inbook = xlrd.open_workbook(infile)
List = inbook.sheet_by_index(0)
for rowx in range(1,List.nrows):
    row = List.row_values(rowx)
    Jitter.append(row[3])
    Picture.append(row[4])
    Duration.append(row[5])
    ISI.append(row[6])
    correctseth.append(row[8])
    Target.append(row[9])


inbook = xlrd.open_workbook(infile)
List = inbook.sheet_by_index(0)
procIdx = []
for rowx in range(1,9):
    row = List.row_values(rowx)
    indices = row[11]
    procLine, aa = indices.split(":")
    procIdx.append(int(procLine))

# index of trial number and block number
trialIdx = 0
blockIdx = 0

# parse out the duration of trial and inter-trial
TrialDuration = [x/1000 for x in Duration]
ITDuration = [x/1000 + y/1000 for x,y in zip(ISI,Jitter)]









# Open LabRecorder
#os.system(".\lib\LabRecorder\LabRecorder.exe")

# Add lsl keypress markers
from pylsl import StreamInfo, StreamInlet, StreamOutlet, resolve_stream
info = StreamInfo(name='BluegrassMemoryExperiment', type='Markers', channel_count=1,
                  channel_format='string', source_id='Keyboard')
# Initialize the keyboard stream.
outlet = StreamOutlet(info)


# LSL for feedback stream
#streams = resolve_stream('name', 'feedbackStream')
#if len(streams)>0:
#    inlet = StreamInlet(streams[0])
# Open LabRecorder
#os.system(".\lib\LabRecorder\LabRecorder.exe")


#currentTime = expInfo['date']
#subjectID = expInfo['participant']
#Labrecorder = '.\lib\LabRecorder\LabRecorderCLI.exe'
#Dataset='.\Dataset'

# Open LabRecorder
#import subprocess, sys, os, winpexpect, time
#child =  winpexpect.winspawn('%s %s\%s_%s.xdf \'name="Keyboard"\'' % (Labrecorder,Dataset,subjectID,currentTime))

# visual and audio stimuli

AudiovisualCue = bool(int(expInfo['Audiovisual Cue']))

import toneplayer
tone = toneplayer.toneplayer()
greenDotOpac = 0
redDotOpac = 0



greenFBSize = 0
redFBSize = 0
# send markers to serial port
import serial
import time

# check if a com port is selected to send markers
isSerial = expInfo['COM Port Marker Receiver']
if isSerial != '':
    port_serial = serial.Serial(isSerial, baudrate=115200)
# keep track of which components have finished
initiationComponents = []
for thisComponent in initiationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initiationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initiation"-------
while continueRoutine:
    # get current time
    t = initiationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initiationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initiationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initiation"-------
for thisComponent in initiationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initiation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "description_A1_1"-------
continueRoutine = True
# update component parameters for each repeat
keyPressRun_1.keys = []
keyPressRun_1.rt = []
_keyPressRun_1_allKeys = []
# keep track of which components have finished
description_A1_1Components = [polygon_1, descriptionText_1, keyPressRun_1]
for thisComponent in description_A1_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
description_A1_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "description_A1_1"-------
while continueRoutine:
    # get current time
    t = description_A1_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=description_A1_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_1* updates
    if polygon_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_1.frameNStart = frameN  # exact frame index
        polygon_1.tStart = t  # local t and not account for scr refresh
        polygon_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_1, 'tStartRefresh')  # time at next scr refresh
        polygon_1.setAutoDraw(True)
    
    # *descriptionText_1* updates
    if descriptionText_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionText_1.frameNStart = frameN  # exact frame index
        descriptionText_1.tStart = t  # local t and not account for scr refresh
        descriptionText_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionText_1, 'tStartRefresh')  # time at next scr refresh
        descriptionText_1.setAutoDraw(True)
    
    # *keyPressRun_1* updates
    if keyPressRun_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyPressRun_1.frameNStart = frameN  # exact frame index
        keyPressRun_1.tStart = t  # local t and not account for scr refresh
        keyPressRun_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyPressRun_1, 'tStartRefresh')  # time at next scr refresh
        keyPressRun_1.status = STARTED
        # keyboard checking is just starting
        keyPressRun_1.clock.reset()  # now t=0
        keyPressRun_1.clearEvents(eventType='keyboard')
    if keyPressRun_1.status == STARTED:
        theseKeys = keyPressRun_1.getKeys(keyList=['space'], waitRelease=False)
        _keyPressRun_1_allKeys.extend(theseKeys)
        if len(_keyPressRun_1_allKeys):
            keyPressRun_1.keys = _keyPressRun_1_allKeys[-1].name  # just the last key pressed
            keyPressRun_1.rt = _keyPressRun_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in description_A1_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "description_A1_1"-------
for thisComponent in description_A1_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_1.started', polygon_1.tStartRefresh)
thisExp.addData('polygon_1.stopped', polygon_1.tStopRefresh)
thisExp.addData('descriptionText_1.started', descriptionText_1.tStartRefresh)
thisExp.addData('descriptionText_1.stopped', descriptionText_1.tStopRefresh)
# check responses
if keyPressRun_1.keys in ['', [], None]:  # No response was made
    keyPressRun_1.keys = None
thisExp.addData('keyPressRun_1.keys',keyPressRun_1.keys)
if keyPressRun_1.keys != None:  # we had a response
    thisExp.addData('keyPressRun_1.rt', keyPressRun_1.rt)
thisExp.addData('keyPressRun_1.started', keyPressRun_1.tStart)
thisExp.addData('keyPressRun_1.stopped', keyPressRun_1.tStop)
thisExp.nextEntry()
# the Routine "description_A1_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation10"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
fixationImage10.setSize(pictureSize)
# keep track of which components have finished
Fixation10Components = [fixation10, fixationImage10, text, text_2, text_3]
for thisComponent in Fixation10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Fixation10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Fixation10"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Fixation10Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Fixation10Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation10* updates
    if fixation10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation10.frameNStart = frameN  # exact frame index
        fixation10.tStart = t  # local t and not account for scr refresh
        fixation10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation10, 'tStartRefresh')  # time at next scr refresh
        fixation10.setAutoDraw(True)
    if fixation10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation10.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            fixation10.tStop = t  # not accounting for scr refresh
            fixation10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation10, 'tStopRefresh')  # time at next scr refresh
            fixation10.setAutoDraw(False)
    
    # *fixationImage10* updates
    if fixationImage10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixationImage10.frameNStart = frameN  # exact frame index
        fixationImage10.tStart = t  # local t and not account for scr refresh
        fixationImage10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixationImage10, 'tStartRefresh')  # time at next scr refresh
        fixationImage10.setAutoDraw(True)
    if fixationImage10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixationImage10.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            fixationImage10.tStop = t  # not accounting for scr refresh
            fixationImage10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixationImage10, 'tStopRefresh')  # time at next scr refresh
            fixationImage10.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fixation10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fixation10"-------
for thisComponent in Fixation10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation10.started', fixation10.tStartRefresh)
thisExp.addData('fixation10.stopped', fixation10.tStopRefresh)
thisExp.addData('fixationImage10.started', fixationImage10.tStartRefresh)
thisExp.addData('fixationImage10.stopped', fixationImage10.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# set up handler to look after randomisation of conditions etc
A1_Blocks = data.TrialHandler(nReps=numBlocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='A1_Blocks')
thisExp.addLoop(A1_Blocks)  # add the loop to the experiment
thisA1_Block = A1_Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisA1_Block.rgb)
if thisA1_Block != None:
    for paramName in thisA1_Block:
        exec('{} = thisA1_Block[paramName]'.format(paramName))

for thisA1_Block in A1_Blocks:
    currentLoop = A1_Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisA1_Block.rgb)
    if thisA1_Block != None:
        for paramName in thisA1_Block:
            exec('{} = thisA1_Block[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Procedure1"-------
    continueRoutine = True
    # update component parameters for each repeat
    index = procIdx[blockIdx]+trialIdx-1
    
    
    
    
    
    greenProc.setSize(greenSize)
    ProcTarget.setSize(pictureSize)
    ProcTarget.setImage(Target[index])
    ProcPicture.setSize(pictureSize)
    ProcPicture.setImage(Picture[index])
    # Send trial onset marker to LSL
    outlet.push_sample('b')
    
    
    # Send trial onset marker to serial port
    if isSerial != '':
        port_serial.write(b'b')
    # keep track of which components have finished
    Procedure1Components = [blackProc, greenProc, ProcTarget, ProcPicture]
    for thisComponent in Procedure1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Procedure1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Procedure1"-------
    while continueRoutine:
        # get current time
        t = Procedure1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Procedure1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blackProc* updates
        if blackProc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackProc.frameNStart = frameN  # exact frame index
            blackProc.tStart = t  # local t and not account for scr refresh
            blackProc.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackProc, 'tStartRefresh')  # time at next scr refresh
            blackProc.setAutoDraw(True)
        if blackProc.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blackProc.tStartRefresh + TrialDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                blackProc.tStop = t  # not accounting for scr refresh
                blackProc.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blackProc, 'tStopRefresh')  # time at next scr refresh
                blackProc.setAutoDraw(False)
        
        # *greenProc* updates
        if greenProc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greenProc.frameNStart = frameN  # exact frame index
            greenProc.tStart = t  # local t and not account for scr refresh
            greenProc.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greenProc, 'tStartRefresh')  # time at next scr refresh
            greenProc.setAutoDraw(True)
        if greenProc.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > greenProc.tStartRefresh + TrialDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                greenProc.tStop = t  # not accounting for scr refresh
                greenProc.frameNStop = frameN  # exact frame index
                win.timeOnFlip(greenProc, 'tStopRefresh')  # time at next scr refresh
                greenProc.setAutoDraw(False)
        
        # *ProcTarget* updates
        if ProcTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ProcTarget.frameNStart = frameN  # exact frame index
            ProcTarget.tStart = t  # local t and not account for scr refresh
            ProcTarget.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ProcTarget, 'tStartRefresh')  # time at next scr refresh
            ProcTarget.setAutoDraw(True)
        if ProcTarget.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ProcTarget.tStartRefresh + TrialDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                ProcTarget.tStop = t  # not accounting for scr refresh
                ProcTarget.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ProcTarget, 'tStopRefresh')  # time at next scr refresh
                ProcTarget.setAutoDraw(False)
        
        # *ProcPicture* updates
        if ProcPicture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ProcPicture.frameNStart = frameN  # exact frame index
            ProcPicture.tStart = t  # local t and not account for scr refresh
            ProcPicture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ProcPicture, 'tStartRefresh')  # time at next scr refresh
            ProcPicture.setAutoDraw(True)
        if ProcPicture.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ProcPicture.tStartRefresh + TrialDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                ProcPicture.tStop = t  # not accounting for scr refresh
                ProcPicture.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ProcPicture, 'tStopRefresh')  # time at next scr refresh
                ProcPicture.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Procedure1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Procedure1"-------
    for thisComponent in Procedure1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    A1_Blocks.addData('blackProc.started', blackProc.tStartRefresh)
    A1_Blocks.addData('blackProc.stopped', blackProc.tStopRefresh)
    A1_Blocks.addData('greenProc.started', greenProc.tStartRefresh)
    A1_Blocks.addData('greenProc.stopped', greenProc.tStopRefresh)
    A1_Blocks.addData('ProcTarget.started', ProcTarget.tStartRefresh)
    A1_Blocks.addData('ProcTarget.stopped', ProcTarget.tStopRefresh)
    A1_Blocks.addData('ProcPicture.started', ProcPicture.tStartRefresh)
    A1_Blocks.addData('ProcPicture.stopped', ProcPicture.tStopRefresh)
    # the Routine "Procedure1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "waitInterTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    whiteWaitInterTrial.setSize(pictureSize)
    # keep track of which components have finished
    waitInterTrialComponents = [blackWaitInterTrial, whiteWaitInterTrial]
    for thisComponent in waitInterTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    waitInterTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "waitInterTrial"-------
    while continueRoutine:
        # get current time
        t = waitInterTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=waitInterTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blackWaitInterTrial* updates
        if blackWaitInterTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackWaitInterTrial.frameNStart = frameN  # exact frame index
            blackWaitInterTrial.tStart = t  # local t and not account for scr refresh
            blackWaitInterTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackWaitInterTrial, 'tStartRefresh')  # time at next scr refresh
            blackWaitInterTrial.setAutoDraw(True)
        if blackWaitInterTrial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blackWaitInterTrial.tStartRefresh + ITDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                blackWaitInterTrial.tStop = t  # not accounting for scr refresh
                blackWaitInterTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blackWaitInterTrial, 'tStopRefresh')  # time at next scr refresh
                blackWaitInterTrial.setAutoDraw(False)
        
        # *whiteWaitInterTrial* updates
        if whiteWaitInterTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            whiteWaitInterTrial.frameNStart = frameN  # exact frame index
            whiteWaitInterTrial.tStart = t  # local t and not account for scr refresh
            whiteWaitInterTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whiteWaitInterTrial, 'tStartRefresh')  # time at next scr refresh
            whiteWaitInterTrial.setAutoDraw(True)
        if whiteWaitInterTrial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > whiteWaitInterTrial.tStartRefresh + ITDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                whiteWaitInterTrial.tStop = t  # not accounting for scr refresh
                whiteWaitInterTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(whiteWaitInterTrial, 'tStopRefresh')  # time at next scr refresh
                whiteWaitInterTrial.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitInterTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "waitInterTrial"-------
    for thisComponent in waitInterTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    A1_Blocks.addData('blackWaitInterTrial.started', blackWaitInterTrial.tStartRefresh)
    A1_Blocks.addData('blackWaitInterTrial.stopped', blackWaitInterTrial.tStopRefresh)
    A1_Blocks.addData('whiteWaitInterTrial.started', whiteWaitInterTrial.tStartRefresh)
    A1_Blocks.addData('whiteWaitInterTrial.stopped', whiteWaitInterTrial.tStopRefresh)
    # the Routine "waitInterTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    A1_trials = data.TrialHandler(nReps=numTrials, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='A1_trials')
    thisExp.addLoop(A1_trials)  # add the loop to the experiment
    thisA1_trial = A1_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisA1_trial.rgb)
    if thisA1_trial != None:
        for paramName in thisA1_trial:
            exec('{} = thisA1_trial[paramName]'.format(paramName))
    
    for thisA1_trial in A1_trials:
        currentLoop = A1_trials
        # abbreviate parameter names if possible (e.g. rgb = thisA1_trial.rgb)
        if thisA1_trial != None:
            for paramName in thisA1_trial:
                exec('{} = thisA1_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "TrialList"-------
        continueRoutine = True
        # update component parameters for each repeat
        index = index + 1
        
        TrialPicture.setSize(pictureSize)
        TrialPicture.setImage(Picture[index])
        keyPressTrial_1.keys = []
        keyPressTrial_1.rt = []
        _keyPressTrial_1_allKeys = []
        # Send trial onset marker to LSL
        #outlet.push_sample('t')
        outlet.push_sample(correctseth[index])
        PressedYet = 0
        
        
        # Send trial onset marker to serial port
        if isSerial != '':
            markerStimSerial = correctseth[index]
            port_serial.write(markerStimSerial.encode())
        # keep track of which components have finished
        TrialListComponents = [blackTrial, whiteTrial, TrialPicture, keyPressTrial_1, green_1, red_1]
        for thisComponent in TrialListComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TrialListClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TrialList"-------
        while continueRoutine:
            # get current time
            t = TrialListClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TrialListClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blackTrial* updates
            if blackTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blackTrial.frameNStart = frameN  # exact frame index
                blackTrial.tStart = t  # local t and not account for scr refresh
                blackTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blackTrial, 'tStartRefresh')  # time at next scr refresh
                blackTrial.setAutoDraw(True)
            if blackTrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blackTrial.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    blackTrial.tStop = t  # not accounting for scr refresh
                    blackTrial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blackTrial, 'tStopRefresh')  # time at next scr refresh
                    blackTrial.setAutoDraw(False)
            
            # *whiteTrial* updates
            if whiteTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                whiteTrial.frameNStart = frameN  # exact frame index
                whiteTrial.tStart = t  # local t and not account for scr refresh
                whiteTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(whiteTrial, 'tStartRefresh')  # time at next scr refresh
                whiteTrial.setAutoDraw(True)
            if whiteTrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > whiteTrial.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    whiteTrial.tStop = t  # not accounting for scr refresh
                    whiteTrial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(whiteTrial, 'tStopRefresh')  # time at next scr refresh
                    whiteTrial.setAutoDraw(False)
            
            # *TrialPicture* updates
            if TrialPicture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialPicture.frameNStart = frameN  # exact frame index
                TrialPicture.tStart = t  # local t and not account for scr refresh
                TrialPicture.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialPicture, 'tStartRefresh')  # time at next scr refresh
                TrialPicture.setAutoDraw(True)
            if TrialPicture.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TrialPicture.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    TrialPicture.tStop = t  # not accounting for scr refresh
                    TrialPicture.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TrialPicture, 'tStopRefresh')  # time at next scr refresh
                    TrialPicture.setAutoDraw(False)
            
            # *keyPressTrial_1* updates
            if keyPressTrial_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyPressTrial_1.frameNStart = frameN  # exact frame index
                keyPressTrial_1.tStart = t  # local t and not account for scr refresh
                keyPressTrial_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyPressTrial_1, 'tStartRefresh')  # time at next scr refresh
                keyPressTrial_1.status = STARTED
                # keyboard checking is just starting
                keyPressTrial_1.clock.reset()  # now t=0
                keyPressTrial_1.clearEvents(eventType='keyboard')
            if keyPressTrial_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyPressTrial_1.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    keyPressTrial_1.tStop = t  # not accounting for scr refresh
                    keyPressTrial_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(keyPressTrial_1, 'tStopRefresh')  # time at next scr refresh
                    keyPressTrial_1.status = FINISHED
            if keyPressTrial_1.status == STARTED:
                theseKeys = keyPressTrial_1.getKeys(keyList=None, waitRelease=False)
                _keyPressTrial_1_allKeys.extend(theseKeys)
                if len(_keyPressTrial_1_allKeys):
                    keyPressTrial_1.keys = _keyPressTrial_1_allKeys[0].name  # just the first key pressed
                    keyPressTrial_1.rt = _keyPressTrial_1_allKeys[0].rt
            # Send trial onset marker to LSL
            if ((keyPressTrial_1.keys) and (not PressedYet)):
                if correctseth[index] == str(keyPressTrial_1.keys)[0]:
                    outlet.push_sample('1')
                    
                    if AudiovisualCue:
                        tone.correct()
                        greenDotOpac = 1
                    #print('correct')
                else:
                    outlet.push_sample('2')
                    
                    if AudiovisualCue:
                        tone.incorrect()
                        redDotOpac = 1
                    #print('incorrect')
                PressedYet = 1
            
            
            # *green_1* updates
            if green_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_1.frameNStart = frameN  # exact frame index
                green_1.tStart = t  # local t and not account for scr refresh
                green_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_1, 'tStartRefresh')  # time at next scr refresh
                green_1.setAutoDraw(True)
            if green_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > green_1.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    green_1.tStop = t  # not accounting for scr refresh
                    green_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(green_1, 'tStopRefresh')  # time at next scr refresh
                    green_1.setAutoDraw(False)
            if green_1.status == STARTED:  # only update if drawing
                green_1.setOpacity(greenDotOpac)
            
            # *red_1* updates
            if red_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_1.frameNStart = frameN  # exact frame index
                red_1.tStart = t  # local t and not account for scr refresh
                red_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_1, 'tStartRefresh')  # time at next scr refresh
                red_1.setAutoDraw(True)
            if red_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_1.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    red_1.tStop = t  # not accounting for scr refresh
                    red_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(red_1, 'tStopRefresh')  # time at next scr refresh
                    red_1.setAutoDraw(False)
            if red_1.status == STARTED:  # only update if drawing
                red_1.setOpacity(redDotOpac)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialListComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TrialList"-------
        for thisComponent in TrialListComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        A1_trials.addData('blackTrial.started', blackTrial.tStartRefresh)
        A1_trials.addData('blackTrial.stopped', blackTrial.tStopRefresh)
        A1_trials.addData('whiteTrial.started', whiteTrial.tStartRefresh)
        A1_trials.addData('whiteTrial.stopped', whiteTrial.tStopRefresh)
        A1_trials.addData('TrialPicture.started', TrialPicture.tStartRefresh)
        A1_trials.addData('TrialPicture.stopped', TrialPicture.tStopRefresh)
        # check responses
        if keyPressTrial_1.keys in ['', [], None]:  # No response was made
            keyPressTrial_1.keys = None
        A1_trials.addData('keyPressTrial_1.keys',keyPressTrial_1.keys)
        if keyPressTrial_1.keys != None:  # we had a response
            A1_trials.addData('keyPressTrial_1.rt', keyPressTrial_1.rt)
        A1_trials.addData('keyPressTrial_1.started', keyPressTrial_1.tStart)
        A1_trials.addData('keyPressTrial_1.stopped', keyPressTrial_1.tStop)
        greenDotOpac = 0
        redDotOpac = 0
        
        
        
        # Send trial onset marker to LSL
        outlet.push_sample('n')
        A1_trials.addData('green_1.started', green_1.tStartRefresh)
        A1_trials.addData('green_1.stopped', green_1.tStopRefresh)
        A1_trials.addData('red_1.started', red_1.tStartRefresh)
        A1_trials.addData('red_1.stopped', red_1.tStopRefresh)
        # the Routine "TrialList" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback_1"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        Feedback_1Components = []
        for thisComponent in Feedback_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Feedback_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Feedback_1"-------
        while continueRoutine:
            # get current time
            t = Feedback_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Feedback_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            feedbackDelay = 0
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback_1"-------
        for thisComponent in Feedback_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Feedback_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "InterTrial"-------
        continueRoutine = True
        # update component parameters for each repeat
        whiteWaitInterTrial_2.setSize(pictureSize)
        keyPressTrial_3.keys = []
        keyPressTrial_3.rt = []
        _keyPressTrial_3_allKeys = []
        
        
        # keep track of which components have finished
        InterTrialComponents = [blackWaitInterTrial_2, whiteWaitInterTrial_2, green_fb_1, red_fb_1, keyPressTrial_3, green_3, red_3]
        for thisComponent in InterTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        InterTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "InterTrial"-------
        while continueRoutine:
            # get current time
            t = InterTrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=InterTrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blackWaitInterTrial_2* updates
            if blackWaitInterTrial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blackWaitInterTrial_2.frameNStart = frameN  # exact frame index
                blackWaitInterTrial_2.tStart = t  # local t and not account for scr refresh
                blackWaitInterTrial_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blackWaitInterTrial_2, 'tStartRefresh')  # time at next scr refresh
                blackWaitInterTrial_2.setAutoDraw(True)
            if blackWaitInterTrial_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blackWaitInterTrial_2.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    blackWaitInterTrial_2.tStop = t  # not accounting for scr refresh
                    blackWaitInterTrial_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blackWaitInterTrial_2, 'tStopRefresh')  # time at next scr refresh
                    blackWaitInterTrial_2.setAutoDraw(False)
            
            # *whiteWaitInterTrial_2* updates
            if whiteWaitInterTrial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                whiteWaitInterTrial_2.frameNStart = frameN  # exact frame index
                whiteWaitInterTrial_2.tStart = t  # local t and not account for scr refresh
                whiteWaitInterTrial_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(whiteWaitInterTrial_2, 'tStartRefresh')  # time at next scr refresh
                whiteWaitInterTrial_2.setAutoDraw(True)
            if whiteWaitInterTrial_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > whiteWaitInterTrial_2.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    whiteWaitInterTrial_2.tStop = t  # not accounting for scr refresh
                    whiteWaitInterTrial_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(whiteWaitInterTrial_2, 'tStopRefresh')  # time at next scr refresh
                    whiteWaitInterTrial_2.setAutoDraw(False)
            
            # *green_fb_1* updates
            if green_fb_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_fb_1.frameNStart = frameN  # exact frame index
                green_fb_1.tStart = t  # local t and not account for scr refresh
                green_fb_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_fb_1, 'tStartRefresh')  # time at next scr refresh
                green_fb_1.setAutoDraw(True)
            if green_fb_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > green_fb_1.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    green_fb_1.tStop = t  # not accounting for scr refresh
                    green_fb_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(green_fb_1, 'tStopRefresh')  # time at next scr refresh
                    green_fb_1.setAutoDraw(False)
            if green_fb_1.status == STARTED:  # only update if drawing
                green_fb_1.setOpacity(greenDotOpac)
                green_fb_1.setSize((greenFBSize, greenFBSize))
            
            # *red_fb_1* updates
            if red_fb_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_fb_1.frameNStart = frameN  # exact frame index
                red_fb_1.tStart = t  # local t and not account for scr refresh
                red_fb_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_fb_1, 'tStartRefresh')  # time at next scr refresh
                red_fb_1.setAutoDraw(True)
            if red_fb_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_fb_1.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    red_fb_1.tStop = t  # not accounting for scr refresh
                    red_fb_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(red_fb_1, 'tStopRefresh')  # time at next scr refresh
                    red_fb_1.setAutoDraw(False)
            if red_fb_1.status == STARTED:  # only update if drawing
                red_fb_1.setOpacity(redDotOpac)
                red_fb_1.setSize((redFBSize, redFBSize))
            
            # *keyPressTrial_3* updates
            if keyPressTrial_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyPressTrial_3.frameNStart = frameN  # exact frame index
                keyPressTrial_3.tStart = t  # local t and not account for scr refresh
                keyPressTrial_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyPressTrial_3, 'tStartRefresh')  # time at next scr refresh
                keyPressTrial_3.status = STARTED
                # keyboard checking is just starting
                keyPressTrial_3.clock.reset()  # now t=0
                keyPressTrial_3.clearEvents(eventType='keyboard')
            if keyPressTrial_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyPressTrial_3.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    keyPressTrial_3.tStop = t  # not accounting for scr refresh
                    keyPressTrial_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(keyPressTrial_3, 'tStopRefresh')  # time at next scr refresh
                    keyPressTrial_3.status = FINISHED
            if keyPressTrial_3.status == STARTED:
                theseKeys = keyPressTrial_3.getKeys(keyList=None, waitRelease=False)
                _keyPressTrial_3_allKeys.extend(theseKeys)
                if len(_keyPressTrial_3_allKeys):
                    keyPressTrial_3.keys = _keyPressTrial_3_allKeys[0].name  # just the first key pressed
                    keyPressTrial_3.rt = _keyPressTrial_3_allKeys[0].rt
            # Send trial onset marker to LSL
            if ((keyPressTrial_3.keys) and (not PressedYet)):
                if correctseth[index] == str(keyPressTrial_3.keys)[0]:
                    outlet.push_sample('1')
                    
                    if AudiovisualCue:
                        tone.correct()
                        greenDotOpac = 1
                    #print('correct')
                else:
                    outlet.push_sample('2')
                    
                    if AudiovisualCue:
                        tone.incorrect()
                        redDotOpac = 1
                    #print('incorrect')
                PressedYet = 1
            
            
            # *green_3* updates
            if green_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_3.frameNStart = frameN  # exact frame index
                green_3.tStart = t  # local t and not account for scr refresh
                green_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_3, 'tStartRefresh')  # time at next scr refresh
                green_3.setAutoDraw(True)
            if green_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > green_3.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    green_3.tStop = t  # not accounting for scr refresh
                    green_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(green_3, 'tStopRefresh')  # time at next scr refresh
                    green_3.setAutoDraw(False)
            if green_3.status == STARTED:  # only update if drawing
                green_3.setOpacity(greenDotOpac)
            
            # *red_3* updates
            if red_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_3.frameNStart = frameN  # exact frame index
                red_3.tStart = t  # local t and not account for scr refresh
                red_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_3, 'tStartRefresh')  # time at next scr refresh
                red_3.setAutoDraw(True)
            if red_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_3.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    red_3.tStop = t  # not accounting for scr refresh
                    red_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(red_3, 'tStopRefresh')  # time at next scr refresh
                    red_3.setAutoDraw(False)
            if red_3.status == STARTED:  # only update if drawing
                red_3.setOpacity(redDotOpac)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InterTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "InterTrial"-------
        for thisComponent in InterTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        A1_trials.addData('blackWaitInterTrial_2.started', blackWaitInterTrial_2.tStartRefresh)
        A1_trials.addData('blackWaitInterTrial_2.stopped', blackWaitInterTrial_2.tStopRefresh)
        A1_trials.addData('whiteWaitInterTrial_2.started', whiteWaitInterTrial_2.tStartRefresh)
        A1_trials.addData('whiteWaitInterTrial_2.stopped', whiteWaitInterTrial_2.tStopRefresh)
        A1_trials.addData('green_fb_1.started', green_fb_1.tStartRefresh)
        A1_trials.addData('green_fb_1.stopped', green_fb_1.tStopRefresh)
        A1_trials.addData('red_fb_1.started', red_fb_1.tStartRefresh)
        A1_trials.addData('red_fb_1.stopped', red_fb_1.tStopRefresh)
        # check responses
        if keyPressTrial_3.keys in ['', [], None]:  # No response was made
            keyPressTrial_3.keys = None
        A1_trials.addData('keyPressTrial_3.keys',keyPressTrial_3.keys)
        if keyPressTrial_3.keys != None:  # we had a response
            A1_trials.addData('keyPressTrial_3.rt', keyPressTrial_3.rt)
        A1_trials.addData('keyPressTrial_3.started', keyPressTrial_3.tStart)
        A1_trials.addData('keyPressTrial_3.stopped', keyPressTrial_3.tStop)
        greenDotOpac = 0
        redDotOpac = 0
        
        greenFBSize = 0
        redFBSize = 0
        A1_trials.addData('green_3.started', green_3.tStartRefresh)
        A1_trials.addData('green_3.stopped', green_3.tStopRefresh)
        A1_trials.addData('red_3.started', red_3.tStartRefresh)
        A1_trials.addData('red_3.stopped', red_3.tStopRefresh)
        # the Routine "InterTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numTrials repeats of 'A1_trials'
    
    
    # ------Prepare to start Routine "Fixation"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    fixationImage.setSize(pictureSize)
    blockIdx = blockIdx + 1
    # keep track of which components have finished
    FixationComponents = [fixation, fixationImage]
    for thisComponent in FixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *fixationImage* updates
        if fixationImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationImage.frameNStart = frameN  # exact frame index
            fixationImage.tStart = t  # local t and not account for scr refresh
            fixationImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationImage, 'tStartRefresh')  # time at next scr refresh
            fixationImage.setAutoDraw(True)
        if fixationImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationImage.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fixationImage.tStop = t  # not accounting for scr refresh
                fixationImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationImage, 'tStopRefresh')  # time at next scr refresh
                fixationImage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Fixation"-------
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    A1_Blocks.addData('fixation.started', fixation.tStartRefresh)
    A1_Blocks.addData('fixation.stopped', fixation.tStopRefresh)
    A1_Blocks.addData('fixationImage.started', fixationImage.tStartRefresh)
    A1_Blocks.addData('fixationImage.stopped', fixationImage.tStopRefresh)
    thisExp.nextEntry()
    
# completed numBlocks repeats of 'A1_Blocks'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
# outlet.push_sample('e')
# keep track of which components have finished
endComponents = [polygon_end, end_text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_end* updates
    if polygon_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_end.frameNStart = frameN  # exact frame index
        polygon_end.tStart = t  # local t and not account for scr refresh
        polygon_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_end, 'tStartRefresh')  # time at next scr refresh
        polygon_end.setAutoDraw(True)
    if polygon_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_end.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            polygon_end.tStop = t  # not accounting for scr refresh
            polygon_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_end, 'tStopRefresh')  # time at next scr refresh
            polygon_end.setAutoDraw(False)
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text, 'tStopRefresh')  # time at next scr refresh
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_end.started', polygon_end.tStartRefresh)
thisExp.addData('polygon_end.stopped', polygon_end.tStopRefresh)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)

# ------Prepare to start Routine "initiation_2"-------
continueRoutine = True
# update component parameters for each repeat





if expInfo['Experiment Mode'] == 'train-A': 
    # Read stimuli excel file
    if expInfo['Handedness'] in ['Right-handed', 'Ambidextrous']:
        infile = './lib/listA2_Lefty.xlsx'
    elif expInfo['Handedness'] in ['Left-handed']:
        infile = './lib/listA2_Righty.xlsx'
    # Number of stimuli
    numBlocks = 8
    numTrials = 20
    
elif expInfo['Experiment Mode'] == 'train-B': 
    # Read stimuli excel file
    if expInfo['Handedness'] in ['Right-handed', 'Ambidextrous']:
        infile = './lib/listA4_Lefty.xlsx'
    elif expInfo['Handedness'] in ['Left-handed']:
        infile = './lib/listA4_Righty.xlsx'
    # Number of stimuli
    numBlocks = 8
    numTrials = 20

elif expInfo['Experiment Mode'] == 'train-A(short)': 
    # Read stimuli excel file
    if expInfo['Handedness'] in ['Right-handed', 'Ambidextrous']:
        infile = './lib/listA2_Lefty.xlsx'
    elif expInfo['Handedness'] in ['Left-handed']:
        infile = './lib/listA2_Righty.xlsx'
    # Number of stimuli
    numBlocks = 8
    numTrials = 12
    
elif expInfo['Experiment Mode'] == 'train-B(short)': 
    # Read stimuli excel file
    if expInfo['Handedness'] in ['Right-handed', 'Ambidextrous']:
        infile = './lib/listA4_Lefty.xlsx'
    elif expInfo['Handedness'] in ['Left-handed']:
        infile = './lib/listA4_Righty.xlsx'
    # Number of stimuli
    numBlocks = 8
    numTrials = 12





Jitter = []
Duration = []
ISI = []
Picture = []
correctseth = []
Target = []
inbook = xlrd.open_workbook(infile)
List = inbook.sheet_by_index(0)
for rowx in range(1,List.nrows):
    row = List.row_values(rowx)
    Jitter.append(row[3])
    Picture.append(row[4])
    Duration.append(row[5])
    ISI.append(row[6])
    correctseth.append(row[8])
    Target.append(row[9])


inbook = xlrd.open_workbook(infile)
List = inbook.sheet_by_index(0)
procIdx = []
for rowx in range(1,9):
    row = List.row_values(rowx)
    indices = row[11]
    procLine, aa = indices.split(":")
    procIdx.append(int(procLine))

# index of trial number and block number
trialIdx = 0
blockIdx = 0

# parse out the duration of trial and inter-trial
TrialDuration = [x/1000 for x in Duration]
ITDuration = [x/1000 + y/1000 for x,y in zip(ISI,Jitter)]

# visual and audio stimuli

import toneplayer
tone = toneplayer.toneplayer()
greenDotOpac = 0
redDotOpac = 0


greenFBSize = 0
redFBSize = 0
# keep track of which components have finished
initiation_2Components = []
for thisComponent in initiation_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initiation_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initiation_2"-------
while continueRoutine:
    # get current time
    t = initiation_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initiation_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initiation_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initiation_2"-------
for thisComponent in initiation_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initiation_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "description_A2_1"-------
continueRoutine = True
# update component parameters for each repeat
keyPressRun_15.keys = []
keyPressRun_15.rt = []
_keyPressRun_15_allKeys = []
# keep track of which components have finished
description_A2_1Components = [polygon_15, descriptionText_15, keyPressRun_15]
for thisComponent in description_A2_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
description_A2_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "description_A2_1"-------
while continueRoutine:
    # get current time
    t = description_A2_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=description_A2_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_15* updates
    if polygon_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_15.frameNStart = frameN  # exact frame index
        polygon_15.tStart = t  # local t and not account for scr refresh
        polygon_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_15, 'tStartRefresh')  # time at next scr refresh
        polygon_15.setAutoDraw(True)
    
    # *descriptionText_15* updates
    if descriptionText_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionText_15.frameNStart = frameN  # exact frame index
        descriptionText_15.tStart = t  # local t and not account for scr refresh
        descriptionText_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionText_15, 'tStartRefresh')  # time at next scr refresh
        descriptionText_15.setAutoDraw(True)
    
    # *keyPressRun_15* updates
    if keyPressRun_15.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyPressRun_15.frameNStart = frameN  # exact frame index
        keyPressRun_15.tStart = t  # local t and not account for scr refresh
        keyPressRun_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyPressRun_15, 'tStartRefresh')  # time at next scr refresh
        keyPressRun_15.status = STARTED
        # keyboard checking is just starting
        keyPressRun_15.clock.reset()  # now t=0
        keyPressRun_15.clearEvents(eventType='keyboard')
    if keyPressRun_15.status == STARTED:
        theseKeys = keyPressRun_15.getKeys(keyList=['space'], waitRelease=False)
        _keyPressRun_15_allKeys.extend(theseKeys)
        if len(_keyPressRun_15_allKeys):
            keyPressRun_15.keys = _keyPressRun_15_allKeys[-1].name  # just the last key pressed
            keyPressRun_15.rt = _keyPressRun_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in description_A2_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "description_A2_1"-------
for thisComponent in description_A2_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_15.started', polygon_15.tStartRefresh)
thisExp.addData('polygon_15.stopped', polygon_15.tStopRefresh)
thisExp.addData('descriptionText_15.started', descriptionText_15.tStartRefresh)
thisExp.addData('descriptionText_15.stopped', descriptionText_15.tStopRefresh)
# check responses
if keyPressRun_15.keys in ['', [], None]:  # No response was made
    keyPressRun_15.keys = None
thisExp.addData('keyPressRun_15.keys',keyPressRun_15.keys)
if keyPressRun_15.keys != None:  # we had a response
    thisExp.addData('keyPressRun_15.rt', keyPressRun_15.rt)
thisExp.addData('keyPressRun_15.started', keyPressRun_15.tStart)
thisExp.addData('keyPressRun_15.stopped', keyPressRun_15.tStop)
thisExp.nextEntry()
# the Routine "description_A2_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation10"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
fixationImage10.setSize(pictureSize)
# keep track of which components have finished
Fixation10Components = [fixation10, fixationImage10, text, text_2, text_3]
for thisComponent in Fixation10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Fixation10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Fixation10"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Fixation10Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Fixation10Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation10* updates
    if fixation10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation10.frameNStart = frameN  # exact frame index
        fixation10.tStart = t  # local t and not account for scr refresh
        fixation10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation10, 'tStartRefresh')  # time at next scr refresh
        fixation10.setAutoDraw(True)
    if fixation10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation10.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            fixation10.tStop = t  # not accounting for scr refresh
            fixation10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation10, 'tStopRefresh')  # time at next scr refresh
            fixation10.setAutoDraw(False)
    
    # *fixationImage10* updates
    if fixationImage10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixationImage10.frameNStart = frameN  # exact frame index
        fixationImage10.tStart = t  # local t and not account for scr refresh
        fixationImage10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixationImage10, 'tStartRefresh')  # time at next scr refresh
        fixationImage10.setAutoDraw(True)
    if fixationImage10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixationImage10.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            fixationImage10.tStop = t  # not accounting for scr refresh
            fixationImage10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixationImage10, 'tStopRefresh')  # time at next scr refresh
            fixationImage10.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fixation10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fixation10"-------
for thisComponent in Fixation10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation10.started', fixation10.tStartRefresh)
thisExp.addData('fixation10.stopped', fixation10.tStopRefresh)
thisExp.addData('fixationImage10.started', fixationImage10.tStartRefresh)
thisExp.addData('fixationImage10.stopped', fixationImage10.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# set up handler to look after randomisation of conditions etc
A2_Blocks = data.TrialHandler(nReps=numBlocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='A2_Blocks')
thisExp.addLoop(A2_Blocks)  # add the loop to the experiment
thisA2_Block = A2_Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisA2_Block.rgb)
if thisA2_Block != None:
    for paramName in thisA2_Block:
        exec('{} = thisA2_Block[paramName]'.format(paramName))

for thisA2_Block in A2_Blocks:
    currentLoop = A2_Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisA2_Block.rgb)
    if thisA2_Block != None:
        for paramName in thisA2_Block:
            exec('{} = thisA2_Block[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Procedure1_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    index = procIdx[blockIdx]+trialIdx-1
    
    
    
    
    
    greenProc_2.setSize(greenSize)
    ProcTarget_2.setSize(pictureSize)
    ProcTarget_2.setImage(Target[index])
    ProcPicture_2.setSize(pictureSize)
    ProcPicture_2.setImage(Picture[index])
    # Send trial onset marker to LSL
    outlet.push_sample('b')
    
    
    
    # Send trial onset marker to serial port
    if isSerial != '':
        port_serial.write(b'b')
    # keep track of which components have finished
    Procedure1_2Components = [blackProc_2, greenProc_2, ProcTarget_2, ProcPicture_2]
    for thisComponent in Procedure1_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Procedure1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Procedure1_2"-------
    while continueRoutine:
        # get current time
        t = Procedure1_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Procedure1_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blackProc_2* updates
        if blackProc_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackProc_2.frameNStart = frameN  # exact frame index
            blackProc_2.tStart = t  # local t and not account for scr refresh
            blackProc_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackProc_2, 'tStartRefresh')  # time at next scr refresh
            blackProc_2.setAutoDraw(True)
        if blackProc_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blackProc_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                blackProc_2.tStop = t  # not accounting for scr refresh
                blackProc_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blackProc_2, 'tStopRefresh')  # time at next scr refresh
                blackProc_2.setAutoDraw(False)
        
        # *greenProc_2* updates
        if greenProc_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greenProc_2.frameNStart = frameN  # exact frame index
            greenProc_2.tStart = t  # local t and not account for scr refresh
            greenProc_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greenProc_2, 'tStartRefresh')  # time at next scr refresh
            greenProc_2.setAutoDraw(True)
        if greenProc_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > greenProc_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                greenProc_2.tStop = t  # not accounting for scr refresh
                greenProc_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(greenProc_2, 'tStopRefresh')  # time at next scr refresh
                greenProc_2.setAutoDraw(False)
        
        # *ProcTarget_2* updates
        if ProcTarget_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ProcTarget_2.frameNStart = frameN  # exact frame index
            ProcTarget_2.tStart = t  # local t and not account for scr refresh
            ProcTarget_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ProcTarget_2, 'tStartRefresh')  # time at next scr refresh
            ProcTarget_2.setAutoDraw(True)
        if ProcTarget_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ProcTarget_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                ProcTarget_2.tStop = t  # not accounting for scr refresh
                ProcTarget_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ProcTarget_2, 'tStopRefresh')  # time at next scr refresh
                ProcTarget_2.setAutoDraw(False)
        
        # *ProcPicture_2* updates
        if ProcPicture_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ProcPicture_2.frameNStart = frameN  # exact frame index
            ProcPicture_2.tStart = t  # local t and not account for scr refresh
            ProcPicture_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ProcPicture_2, 'tStartRefresh')  # time at next scr refresh
            ProcPicture_2.setAutoDraw(True)
        if ProcPicture_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ProcPicture_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                ProcPicture_2.tStop = t  # not accounting for scr refresh
                ProcPicture_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ProcPicture_2, 'tStopRefresh')  # time at next scr refresh
                ProcPicture_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Procedure1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Procedure1_2"-------
    for thisComponent in Procedure1_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    A2_Blocks.addData('blackProc_2.started', blackProc_2.tStartRefresh)
    A2_Blocks.addData('blackProc_2.stopped', blackProc_2.tStopRefresh)
    A2_Blocks.addData('greenProc_2.started', greenProc_2.tStartRefresh)
    A2_Blocks.addData('greenProc_2.stopped', greenProc_2.tStopRefresh)
    A2_Blocks.addData('ProcTarget_2.started', ProcTarget_2.tStartRefresh)
    A2_Blocks.addData('ProcTarget_2.stopped', ProcTarget_2.tStopRefresh)
    A2_Blocks.addData('ProcPicture_2.started', ProcPicture_2.tStartRefresh)
    A2_Blocks.addData('ProcPicture_2.stopped', ProcPicture_2.tStopRefresh)
    # the Routine "Procedure1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "waitInterTrial_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    whiteWaitInterTrial_3.setSize(pictureSize)
    # keep track of which components have finished
    waitInterTrial_2Components = [blackWaitInterTrial_3, whiteWaitInterTrial_3]
    for thisComponent in waitInterTrial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    waitInterTrial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "waitInterTrial_2"-------
    while continueRoutine:
        # get current time
        t = waitInterTrial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=waitInterTrial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blackWaitInterTrial_3* updates
        if blackWaitInterTrial_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackWaitInterTrial_3.frameNStart = frameN  # exact frame index
            blackWaitInterTrial_3.tStart = t  # local t and not account for scr refresh
            blackWaitInterTrial_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackWaitInterTrial_3, 'tStartRefresh')  # time at next scr refresh
            blackWaitInterTrial_3.setAutoDraw(True)
        if blackWaitInterTrial_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blackWaitInterTrial_3.tStartRefresh + ITDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                blackWaitInterTrial_3.tStop = t  # not accounting for scr refresh
                blackWaitInterTrial_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blackWaitInterTrial_3, 'tStopRefresh')  # time at next scr refresh
                blackWaitInterTrial_3.setAutoDraw(False)
        
        # *whiteWaitInterTrial_3* updates
        if whiteWaitInterTrial_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            whiteWaitInterTrial_3.frameNStart = frameN  # exact frame index
            whiteWaitInterTrial_3.tStart = t  # local t and not account for scr refresh
            whiteWaitInterTrial_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whiteWaitInterTrial_3, 'tStartRefresh')  # time at next scr refresh
            whiteWaitInterTrial_3.setAutoDraw(True)
        if whiteWaitInterTrial_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > whiteWaitInterTrial_3.tStartRefresh + ITDuration[index]-frameTolerance:
                # keep track of stop time/frame for later
                whiteWaitInterTrial_3.tStop = t  # not accounting for scr refresh
                whiteWaitInterTrial_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(whiteWaitInterTrial_3, 'tStopRefresh')  # time at next scr refresh
                whiteWaitInterTrial_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitInterTrial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "waitInterTrial_2"-------
    for thisComponent in waitInterTrial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    A2_Blocks.addData('blackWaitInterTrial_3.started', blackWaitInterTrial_3.tStartRefresh)
    A2_Blocks.addData('blackWaitInterTrial_3.stopped', blackWaitInterTrial_3.tStopRefresh)
    A2_Blocks.addData('whiteWaitInterTrial_3.started', whiteWaitInterTrial_3.tStartRefresh)
    A2_Blocks.addData('whiteWaitInterTrial_3.stopped', whiteWaitInterTrial_3.tStopRefresh)
    # the Routine "waitInterTrial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    A2_trials = data.TrialHandler(nReps=numTrials, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='A2_trials')
    thisExp.addLoop(A2_trials)  # add the loop to the experiment
    thisA2_trial = A2_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisA2_trial.rgb)
    if thisA2_trial != None:
        for paramName in thisA2_trial:
            exec('{} = thisA2_trial[paramName]'.format(paramName))
    
    for thisA2_trial in A2_trials:
        currentLoop = A2_trials
        # abbreviate parameter names if possible (e.g. rgb = thisA2_trial.rgb)
        if thisA2_trial != None:
            for paramName in thisA2_trial:
                exec('{} = thisA2_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "TrialList_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        index = index + 1
        
        TrialPicture_2.setSize(pictureSize)
        TrialPicture_2.setImage(Picture[index])
        keyPressTrial_2.keys = []
        keyPressTrial_2.rt = []
        _keyPressTrial_2_allKeys = []
        # Send trial onset marker to LSL
        #outlet.push_sample('t')
        outlet.push_sample(correctseth[index])
        PressedYet = 0
        
        
        
        # Send trial onset marker to serial port
        if isSerial != '':
            markerStimSerial = correctseth[index]
            port_serial.write(markerStimSerial.encode())
        
        # keep track of which components have finished
        TrialList_2Components = [blackTrial_2, whiteTrial_2, TrialPicture_2, keyPressTrial_2, green_2, red_2]
        for thisComponent in TrialList_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TrialList_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TrialList_2"-------
        while continueRoutine:
            # get current time
            t = TrialList_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TrialList_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blackTrial_2* updates
            if blackTrial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blackTrial_2.frameNStart = frameN  # exact frame index
                blackTrial_2.tStart = t  # local t and not account for scr refresh
                blackTrial_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blackTrial_2, 'tStartRefresh')  # time at next scr refresh
                blackTrial_2.setAutoDraw(True)
            if blackTrial_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blackTrial_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    blackTrial_2.tStop = t  # not accounting for scr refresh
                    blackTrial_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blackTrial_2, 'tStopRefresh')  # time at next scr refresh
                    blackTrial_2.setAutoDraw(False)
            
            # *whiteTrial_2* updates
            if whiteTrial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                whiteTrial_2.frameNStart = frameN  # exact frame index
                whiteTrial_2.tStart = t  # local t and not account for scr refresh
                whiteTrial_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(whiteTrial_2, 'tStartRefresh')  # time at next scr refresh
                whiteTrial_2.setAutoDraw(True)
            if whiteTrial_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > whiteTrial_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    whiteTrial_2.tStop = t  # not accounting for scr refresh
                    whiteTrial_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(whiteTrial_2, 'tStopRefresh')  # time at next scr refresh
                    whiteTrial_2.setAutoDraw(False)
            
            # *TrialPicture_2* updates
            if TrialPicture_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialPicture_2.frameNStart = frameN  # exact frame index
                TrialPicture_2.tStart = t  # local t and not account for scr refresh
                TrialPicture_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialPicture_2, 'tStartRefresh')  # time at next scr refresh
                TrialPicture_2.setAutoDraw(True)
            if TrialPicture_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TrialPicture_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    TrialPicture_2.tStop = t  # not accounting for scr refresh
                    TrialPicture_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TrialPicture_2, 'tStopRefresh')  # time at next scr refresh
                    TrialPicture_2.setAutoDraw(False)
            
            # *keyPressTrial_2* updates
            if keyPressTrial_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyPressTrial_2.frameNStart = frameN  # exact frame index
                keyPressTrial_2.tStart = t  # local t and not account for scr refresh
                keyPressTrial_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyPressTrial_2, 'tStartRefresh')  # time at next scr refresh
                keyPressTrial_2.status = STARTED
                # keyboard checking is just starting
                keyPressTrial_2.clock.reset()  # now t=0
                keyPressTrial_2.clearEvents(eventType='keyboard')
            if keyPressTrial_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyPressTrial_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    keyPressTrial_2.tStop = t  # not accounting for scr refresh
                    keyPressTrial_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(keyPressTrial_2, 'tStopRefresh')  # time at next scr refresh
                    keyPressTrial_2.status = FINISHED
            if keyPressTrial_2.status == STARTED:
                theseKeys = keyPressTrial_2.getKeys(keyList=None, waitRelease=False)
                _keyPressTrial_2_allKeys.extend(theseKeys)
                if len(_keyPressTrial_2_allKeys):
                    keyPressTrial_2.keys = _keyPressTrial_2_allKeys[0].name  # just the first key pressed
                    keyPressTrial_2.rt = _keyPressTrial_2_allKeys[0].rt
            # Send trial onset marker to LSL
            if ((keyPressTrial_2.keys) and (not PressedYet)):
                if correctseth[index] == str(keyPressTrial_2.keys)[0]:
                    outlet.push_sample('1')
                    
                    if AudiovisualCue:
                        tone.correct()
                        greenDotOpac = 1
                    #print('correct')
                else:
                    outlet.push_sample('2')
                    
                    if AudiovisualCue:
                        tone.incorrect()
                        redDotOpac = 1
                    #print('incorrect')
                PressedYet = 1
            
            
            # *green_2* updates
            if green_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_2.frameNStart = frameN  # exact frame index
                green_2.tStart = t  # local t and not account for scr refresh
                green_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_2, 'tStartRefresh')  # time at next scr refresh
                green_2.setAutoDraw(True)
            if green_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > green_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    green_2.tStop = t  # not accounting for scr refresh
                    green_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(green_2, 'tStopRefresh')  # time at next scr refresh
                    green_2.setAutoDraw(False)
            if green_2.status == STARTED:  # only update if drawing
                green_2.setOpacity(greenDotOpac)
            
            # *red_2* updates
            if red_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_2.frameNStart = frameN  # exact frame index
                red_2.tStart = t  # local t and not account for scr refresh
                red_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_2, 'tStartRefresh')  # time at next scr refresh
                red_2.setAutoDraw(True)
            if red_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_2.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    red_2.tStop = t  # not accounting for scr refresh
                    red_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(red_2, 'tStopRefresh')  # time at next scr refresh
                    red_2.setAutoDraw(False)
            if red_2.status == STARTED:  # only update if drawing
                red_2.setOpacity(redDotOpac)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialList_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TrialList_2"-------
        for thisComponent in TrialList_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        A2_trials.addData('blackTrial_2.started', blackTrial_2.tStartRefresh)
        A2_trials.addData('blackTrial_2.stopped', blackTrial_2.tStopRefresh)
        A2_trials.addData('whiteTrial_2.started', whiteTrial_2.tStartRefresh)
        A2_trials.addData('whiteTrial_2.stopped', whiteTrial_2.tStopRefresh)
        A2_trials.addData('TrialPicture_2.started', TrialPicture_2.tStartRefresh)
        A2_trials.addData('TrialPicture_2.stopped', TrialPicture_2.tStopRefresh)
        # check responses
        if keyPressTrial_2.keys in ['', [], None]:  # No response was made
            keyPressTrial_2.keys = None
        A2_trials.addData('keyPressTrial_2.keys',keyPressTrial_2.keys)
        if keyPressTrial_2.keys != None:  # we had a response
            A2_trials.addData('keyPressTrial_2.rt', keyPressTrial_2.rt)
        A2_trials.addData('keyPressTrial_2.started', keyPressTrial_2.tStart)
        A2_trials.addData('keyPressTrial_2.stopped', keyPressTrial_2.tStop)
        greenDotOpac = 0
        redDotOpac = 0
        
        
        
        
        # Send trial onset marker to LSL
        outlet.push_sample('n')
        A2_trials.addData('green_2.started', green_2.tStartRefresh)
        A2_trials.addData('green_2.stopped', green_2.tStopRefresh)
        A2_trials.addData('red_2.started', red_2.tStartRefresh)
        A2_trials.addData('red_2.stopped', red_2.tStopRefresh)
        # the Routine "TrialList_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        Feedback_2Components = []
        for thisComponent in Feedback_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Feedback_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Feedback_2"-------
        while continueRoutine:
            # get current time
            t = Feedback_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Feedback_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            feedbackDelay = 0
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback_2"-------
        for thisComponent in Feedback_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Feedback_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "InterTrial_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        whiteWaitInterTrial_4.setSize(pictureSize)
        keyPressTrial_4.keys = []
        keyPressTrial_4.rt = []
        _keyPressTrial_4_allKeys = []
        # keep track of which components have finished
        InterTrial_2Components = [blackWaitInterTrial_4, whiteWaitInterTrial_4, green_fb_2, red_fb_2, keyPressTrial_4, green_4, red_4]
        for thisComponent in InterTrial_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        InterTrial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "InterTrial_2"-------
        while continueRoutine:
            # get current time
            t = InterTrial_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=InterTrial_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blackWaitInterTrial_4* updates
            if blackWaitInterTrial_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blackWaitInterTrial_4.frameNStart = frameN  # exact frame index
                blackWaitInterTrial_4.tStart = t  # local t and not account for scr refresh
                blackWaitInterTrial_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blackWaitInterTrial_4, 'tStartRefresh')  # time at next scr refresh
                blackWaitInterTrial_4.setAutoDraw(True)
            if blackWaitInterTrial_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blackWaitInterTrial_4.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    blackWaitInterTrial_4.tStop = t  # not accounting for scr refresh
                    blackWaitInterTrial_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blackWaitInterTrial_4, 'tStopRefresh')  # time at next scr refresh
                    blackWaitInterTrial_4.setAutoDraw(False)
            
            # *whiteWaitInterTrial_4* updates
            if whiteWaitInterTrial_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                whiteWaitInterTrial_4.frameNStart = frameN  # exact frame index
                whiteWaitInterTrial_4.tStart = t  # local t and not account for scr refresh
                whiteWaitInterTrial_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(whiteWaitInterTrial_4, 'tStartRefresh')  # time at next scr refresh
                whiteWaitInterTrial_4.setAutoDraw(True)
            if whiteWaitInterTrial_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > whiteWaitInterTrial_4.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    whiteWaitInterTrial_4.tStop = t  # not accounting for scr refresh
                    whiteWaitInterTrial_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(whiteWaitInterTrial_4, 'tStopRefresh')  # time at next scr refresh
                    whiteWaitInterTrial_4.setAutoDraw(False)
            
            # *green_fb_2* updates
            if green_fb_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_fb_2.frameNStart = frameN  # exact frame index
                green_fb_2.tStart = t  # local t and not account for scr refresh
                green_fb_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_fb_2, 'tStartRefresh')  # time at next scr refresh
                green_fb_2.setAutoDraw(True)
            if green_fb_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > green_fb_2.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    green_fb_2.tStop = t  # not accounting for scr refresh
                    green_fb_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(green_fb_2, 'tStopRefresh')  # time at next scr refresh
                    green_fb_2.setAutoDraw(False)
            if green_fb_2.status == STARTED:  # only update if drawing
                green_fb_2.setOpacity(greenDotOpac)
                green_fb_2.setSize((greenFBSize, greenFBSize))
            
            # *red_fb_2* updates
            if red_fb_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_fb_2.frameNStart = frameN  # exact frame index
                red_fb_2.tStart = t  # local t and not account for scr refresh
                red_fb_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_fb_2, 'tStartRefresh')  # time at next scr refresh
                red_fb_2.setAutoDraw(True)
            if red_fb_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_fb_2.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    red_fb_2.tStop = t  # not accounting for scr refresh
                    red_fb_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(red_fb_2, 'tStopRefresh')  # time at next scr refresh
                    red_fb_2.setAutoDraw(False)
            if red_fb_2.status == STARTED:  # only update if drawing
                red_fb_2.setOpacity(redDotOpac)
                red_fb_2.setSize((redFBSize, redFBSize))
            
            # *keyPressTrial_4* updates
            if keyPressTrial_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyPressTrial_4.frameNStart = frameN  # exact frame index
                keyPressTrial_4.tStart = t  # local t and not account for scr refresh
                keyPressTrial_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyPressTrial_4, 'tStartRefresh')  # time at next scr refresh
                keyPressTrial_4.status = STARTED
                # keyboard checking is just starting
                keyPressTrial_4.clock.reset()  # now t=0
                keyPressTrial_4.clearEvents(eventType='keyboard')
            if keyPressTrial_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyPressTrial_4.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    keyPressTrial_4.tStop = t  # not accounting for scr refresh
                    keyPressTrial_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(keyPressTrial_4, 'tStopRefresh')  # time at next scr refresh
                    keyPressTrial_4.status = FINISHED
            if keyPressTrial_4.status == STARTED:
                theseKeys = keyPressTrial_4.getKeys(keyList=None, waitRelease=False)
                _keyPressTrial_4_allKeys.extend(theseKeys)
                if len(_keyPressTrial_4_allKeys):
                    keyPressTrial_4.keys = _keyPressTrial_4_allKeys[0].name  # just the first key pressed
                    keyPressTrial_4.rt = _keyPressTrial_4_allKeys[0].rt
            # Send trial onset marker to LSL
            if ((keyPressTrial_4.keys) and (not PressedYet)):
                if correctseth[index] == str(keyPressTrial_4.keys)[0]:
                    outlet.push_sample('1')
                    
                    if AudiovisualCue:
                        tone.correct()
                        greenDotOpac = 1
                    #print('correct')
                else:
                    outlet.push_sample('2')
                    
                    if AudiovisualCue:
                        tone.incorrect()
                        redDotOpac = 1
                    #print('incorrect')
                PressedYet = 1
            
            
            # *green_4* updates
            if green_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_4.frameNStart = frameN  # exact frame index
                green_4.tStart = t  # local t and not account for scr refresh
                green_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_4, 'tStartRefresh')  # time at next scr refresh
                green_4.setAutoDraw(True)
            if green_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > green_4.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    green_4.tStop = t  # not accounting for scr refresh
                    green_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(green_4, 'tStopRefresh')  # time at next scr refresh
                    green_4.setAutoDraw(False)
            if green_4.status == STARTED:  # only update if drawing
                green_4.setOpacity(greenDotOpac)
            
            # *red_4* updates
            if red_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_4.frameNStart = frameN  # exact frame index
                red_4.tStart = t  # local t and not account for scr refresh
                red_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_4, 'tStartRefresh')  # time at next scr refresh
                red_4.setAutoDraw(True)
            if red_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_4.tStartRefresh + ITDuration[index] +  feedbackDelay-frameTolerance:
                    # keep track of stop time/frame for later
                    red_4.tStop = t  # not accounting for scr refresh
                    red_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(red_4, 'tStopRefresh')  # time at next scr refresh
                    red_4.setAutoDraw(False)
            if red_4.status == STARTED:  # only update if drawing
                red_4.setOpacity(redDotOpac)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InterTrial_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "InterTrial_2"-------
        for thisComponent in InterTrial_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        A2_trials.addData('blackWaitInterTrial_4.started', blackWaitInterTrial_4.tStartRefresh)
        A2_trials.addData('blackWaitInterTrial_4.stopped', blackWaitInterTrial_4.tStopRefresh)
        A2_trials.addData('whiteWaitInterTrial_4.started', whiteWaitInterTrial_4.tStartRefresh)
        A2_trials.addData('whiteWaitInterTrial_4.stopped', whiteWaitInterTrial_4.tStopRefresh)
        A2_trials.addData('green_fb_2.started', green_fb_2.tStartRefresh)
        A2_trials.addData('green_fb_2.stopped', green_fb_2.tStopRefresh)
        A2_trials.addData('red_fb_2.started', red_fb_2.tStartRefresh)
        A2_trials.addData('red_fb_2.stopped', red_fb_2.tStopRefresh)
        # check responses
        if keyPressTrial_4.keys in ['', [], None]:  # No response was made
            keyPressTrial_4.keys = None
        A2_trials.addData('keyPressTrial_4.keys',keyPressTrial_4.keys)
        if keyPressTrial_4.keys != None:  # we had a response
            A2_trials.addData('keyPressTrial_4.rt', keyPressTrial_4.rt)
        A2_trials.addData('keyPressTrial_4.started', keyPressTrial_4.tStart)
        A2_trials.addData('keyPressTrial_4.stopped', keyPressTrial_4.tStop)
        greenDotOpac = 0
        redDotOpac = 0
        
        greenFBSize = 0
        redFBSize = 0
        A2_trials.addData('green_4.started', green_4.tStartRefresh)
        A2_trials.addData('green_4.stopped', green_4.tStopRefresh)
        A2_trials.addData('red_4.started', red_4.tStartRefresh)
        A2_trials.addData('red_4.stopped', red_4.tStopRefresh)
        # the Routine "InterTrial_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numTrials repeats of 'A2_trials'
    
    
    # ------Prepare to start Routine "Fixation_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    fixationImage_2.setSize(pictureSize)
    blockIdx = blockIdx + 1
    # keep track of which components have finished
    Fixation_2Components = [fixation_2, fixationImage_2]
    for thisComponent in Fixation_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Fixation_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Fixation_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Fixation_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Fixation_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_2* updates
        if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(True)
        if fixation_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(False)
        
        # *fixationImage_2* updates
        if fixationImage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationImage_2.frameNStart = frameN  # exact frame index
            fixationImage_2.tStart = t  # local t and not account for scr refresh
            fixationImage_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationImage_2, 'tStartRefresh')  # time at next scr refresh
            fixationImage_2.setAutoDraw(True)
        if fixationImage_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationImage_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fixationImage_2.tStop = t  # not accounting for scr refresh
                fixationImage_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationImage_2, 'tStopRefresh')  # time at next scr refresh
                fixationImage_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Fixation_2"-------
    for thisComponent in Fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    A2_Blocks.addData('fixation_2.started', fixation_2.tStartRefresh)
    A2_Blocks.addData('fixation_2.stopped', fixation_2.tStopRefresh)
    A2_Blocks.addData('fixationImage_2.started', fixationImage_2.tStartRefresh)
    A2_Blocks.addData('fixationImage_2.stopped', fixationImage_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed numBlocks repeats of 'A2_Blocks'


# ------Prepare to start Routine "end_2"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('e')


# Send trial onset marker to serial port
if isSerial != '':
    port_serial.write(b'e')

# keep track of which components have finished
end_2Components = [polygon_end_2, end_text_2]
for thisComponent in end_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_end_2* updates
    if polygon_end_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_end_2.frameNStart = frameN  # exact frame index
        polygon_end_2.tStart = t  # local t and not account for scr refresh
        polygon_end_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_end_2, 'tStartRefresh')  # time at next scr refresh
        polygon_end_2.setAutoDraw(True)
    if polygon_end_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_end_2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            polygon_end_2.tStop = t  # not accounting for scr refresh
            polygon_end_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_end_2, 'tStopRefresh')  # time at next scr refresh
            polygon_end_2.setAutoDraw(False)
    
    # *end_text_2* updates
    if end_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text_2.frameNStart = frameN  # exact frame index
        end_text_2.tStart = t  # local t and not account for scr refresh
        end_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text_2, 'tStartRefresh')  # time at next scr refresh
        end_text_2.setAutoDraw(True)
    if end_text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text_2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            end_text_2.tStop = t  # not accounting for scr refresh
            end_text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text_2, 'tStopRefresh')  # time at next scr refresh
            end_text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_2"-------
for thisComponent in end_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_end_2.started', polygon_end_2.tStartRefresh)
thisExp.addData('polygon_end_2.stopped', polygon_end_2.tStopRefresh)
thisExp.addData('end_text_2.started', end_text_2.tStartRefresh)
thisExp.addData('end_text_2.stopped', end_text_2.tStopRefresh)
# child.sendline('\r')

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
