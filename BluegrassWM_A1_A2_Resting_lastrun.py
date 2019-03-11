#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.1),
    on March 11, 2019, at 15:30
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.1'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Projects\\BluegrassWMPlatform_Psychopy\\BluegrassWM_A1_A2_Resting_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=1,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "initiation"
initiationClock = core.Clock()


# Initialize components for Routine "description"
descriptionClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText = visual.TextStim(win=win, name='descriptionText',
    text='A1\nPlease determine whether each image matches one of the images shown with a green border. \nIf it matches,\nplease quickly press the A (L) key.\nIf it does not,\nplease quickly press the L (A) key.\n\nIf a cross (+) appears appears,\nplease quickly press both keys.\n\nPRESS THE SPACEBAR WHEN READY',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

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
    win=win, name='fixationImage10',
    image='./stimuli/images/fix.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


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
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
ProcTarget = visual.ImageStim(
    win=win, name='ProcTarget',
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ProcPicture = visual.ImageStim(
    win=win, name='ProcPicture',
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
    opacity=1, depth=-1.0, interpolate=True)
whiteWaitInterTrial = visual.ImageStim(
    win=win, name='whiteWaitInterTrial',
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

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
    win=win, name='TrialPicture',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


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
    win=win, name='whiteWaitInterTrial_2',
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


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
    win=win, name='fixationImage',
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
    text='Thank you for your \npatience!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);


# Initialize components for Routine "initiation_2"
initiation_2Clock = core.Clock()


# Initialize components for Routine "description_2"
description_2Clock = core.Clock()
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText_2 = visual.TextStim(win=win, name='descriptionText_2',
    text='A2\nPlease determine whether each image matches one of the images shown with a green border. \nIf it matches,\nplease quickly press the A (L) key.\nIf it does not,\nplease quickly press the L (A) key.\n\nIf a cross (+) appears appears,\nplease quickly press both keys.\n\nPRESS THE SPACEBAR WHEN READY',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Fixation10_2"
Fixation10_2Clock = core.Clock()
fixation10_2 = visual.Rect(
    win=win, name='fixation10_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixationImage10_2 = visual.ImageStim(
    win=win, name='fixationImage10_2',
    image='./stimuli/images/fix.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


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
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
ProcTarget_2 = visual.ImageStim(
    win=win, name='ProcTarget_2',
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ProcPicture_2 = visual.ImageStim(
    win=win, name='ProcPicture_2',
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
    opacity=1, depth=-1.0, interpolate=True)
whiteWaitInterTrial_3 = visual.ImageStim(
    win=win, name='whiteWaitInterTrial_3',
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

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
    win=win, name='TrialPicture_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


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
    win=win, name='whiteWaitInterTrial_4',
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


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
    win=win, name='fixationImage_2',
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
    text='Thank you for your \npatience!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);


# Initialize components for Routine "desEyesOpen"
desEyesOpenClock = core.Clock()
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText_3 = visual.TextStim(win=win, name='descriptionText_3',
    text='Eyes open for one minute\nPlease stare at fixation point\n\nTry not to blink during this time\n\nTry to be as still as possible\n\nWe will come in as soon as minute is up',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Fixation10_3"
Fixation10_3Clock = core.Clock()
fixation10_3 = visual.Rect(
    win=win, name='fixation10_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixationImage10_3 = visual.ImageStim(
    win=win, name='fixationImage10_3',
    image='./stimuli/images/fix.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "EyesOpen"
EyesOpenClock = core.Clock()
blackProc_3 = visual.Rect(
    win=win, name='blackProc_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
greenProc_3 = visual.Rect(
    win=win, name='greenProc_3',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
ProcTarget_3 = visual.ImageStim(
    win=win, name='ProcTarget_3',
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
ProcPicture_3 = visual.ImageStim(
    win=win, name='ProcPicture_3',
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


# Initialize components for Routine "waitInterTrial_3"
waitInterTrial_3Clock = core.Clock()

blackWaitInterTrial_5 = visual.Rect(
    win=win, name='blackWaitInterTrial_5',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
whiteWaitInterTrial_5 = visual.ImageStim(
    win=win, name='whiteWaitInterTrial_5',
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "desEyesClose"
desEyesCloseClock = core.Clock()
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText_4 = visual.TextStim(win=win, name='descriptionText_4',
    text='Eyes close for one minute\n\nTry not to blink during this time\n\nTry to be as still as possible\n\nWe will come in as soon as minute is up',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Fixation10_4"
Fixation10_4Clock = core.Clock()
fixation10_4 = visual.Rect(
    win=win, name='fixation10_4',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixationImage10_4 = visual.ImageStim(
    win=win, name='fixationImage10_4',
    image='./stimuli/images/fix.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "EyesClose"
EyesCloseClock = core.Clock()
blackProc_4 = visual.Rect(
    win=win, name='blackProc_4',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
greenProc_4 = visual.Rect(
    win=win, name='greenProc_4',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
ProcTarget_4 = visual.ImageStim(
    win=win, name='ProcTarget_4',
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
ProcPicture_4 = visual.ImageStim(
    win=win, name='ProcPicture_4',
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


# Initialize components for Routine "waitInterTrial_4"
waitInterTrial_4Clock = core.Clock()

blackWaitInterTrial_6 = visual.Rect(
    win=win, name='blackWaitInterTrial_6',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
whiteWaitInterTrial_6 = visual.ImageStim(
    win=win, name='whiteWaitInterTrial_6',
    image='./stimuli/images/blank.bmp', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "end_3"
end_3Clock = core.Clock()
polygon_end_3 = visual.Rect(
    win=win, name='polygon_end_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
end_text_3 = visual.TextStim(win=win, name='end_text_3',
    text='Thank you for your \nparticipation!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "initiation"-------
t = 0
initiationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# Add random and excel library
import random, xlrd, os, sys
sys.path.append('./lib/')



# Open LabRecorder
#os.system(".\lib\LabRecorder\LabRecorder.exe")




# Add lsl keypress markers
from pylsl import StreamInfo, StreamOutlet
info = StreamInfo(name='Keyboard', type='Markers', channel_count=1,
                  channel_format='string', source_id='Keyboard')
# Initialize the keyboard stream.
outlet = StreamOutlet(info)



currentTime = expInfo['date']
subjectID = expInfo['participant']
Labrecorder = '.\lib\LabRecorder\LabRecorderCLI.exe'
Dataset='.\Dataset'

# Open LabRecorder
import subprocess, sys, os, winpexpect, time
#os.system("start /B start cmd.exe @cmd /k .\lib\LabRecorder\LabRecorderCLI.exe .\Dataset\'currentTime'.xdf 'type=EEG'")
#os.system("start /B start cmd.exe @cmd /k %s %s\%s_%s 'type=EEG'" % (Labrecorder, Dataset, currentTime,subjectID))
child =  winpexpect.winspawn('%s %s\%s_%s \'name="Keyboard"\'' % (Labrecorder,Dataset,currentTime,subjectID))



# Fix random seed
random.seed()
# Read stimuli excel file
infile = './lib/listA1.xlsx'
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









# keep track of which components have finished
initiationComponents = []
for thisComponent in initiationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "initiation"-------
while continueRoutine:
    # get current time
    t = initiationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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

# ------Prepare to start Routine "description"-------
t = 0
descriptionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyPressRun = event.BuilderKeyResponse()
# keep track of which components have finished
descriptionComponents = [polygon, descriptionText, keyPressRun]
for thisComponent in descriptionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "description"-------
while continueRoutine:
    # get current time
    t = descriptionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if t >= 0.0 and polygon.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon.tStart = t
        polygon.frameNStart = frameN  # exact frame index
        polygon.setAutoDraw(True)
    
    # *descriptionText* updates
    if t >= 0.0 and descriptionText.status == NOT_STARTED:
        # keep track of start time/frame for later
        descriptionText.tStart = t
        descriptionText.frameNStart = frameN  # exact frame index
        descriptionText.setAutoDraw(True)
    
    # *keyPressRun* updates
    if t >= 0.0 and keyPressRun.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyPressRun.tStart = t
        keyPressRun.frameNStart = frameN  # exact frame index
        keyPressRun.status = STARTED
        # keyboard checking is just starting
        keyPressRun.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if keyPressRun.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            keyPressRun.keys = theseKeys[-1]  # just the last key pressed
            keyPressRun.rt = keyPressRun.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in descriptionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "description"-------
for thisComponent in descriptionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyPressRun.keys in ['', [], None]:  # No response was made
    keyPressRun.keys=None
thisExp.addData('keyPressRun.keys',keyPressRun.keys)
if keyPressRun.keys != None:  # we had a response
    thisExp.addData('keyPressRun.rt', keyPressRun.rt)
thisExp.nextEntry()
# the Routine "description" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation10"-------
t = 0
Fixation10Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
fixationImage10.setSize(pictureSize)
# Send trial onset marker to LSL
outlet.push_sample('f')
# keep track of which components have finished
Fixation10Components = [fixation10, fixationImage10]
for thisComponent in Fixation10Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fixation10"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Fixation10Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation10* updates
    if t >= 0.0 and fixation10.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation10.tStart = t
        fixation10.frameNStart = frameN  # exact frame index
        fixation10.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixation10.status == STARTED and t >= frameRemains:
        fixation10.setAutoDraw(False)
    
    # *fixationImage10* updates
    if t >= 0.0 and fixationImage10.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixationImage10.tStart = t
        fixationImage10.frameNStart = frameN  # exact frame index
        fixationImage10.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixationImage10.status == STARTED and t >= frameRemains:
        fixationImage10.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
    t = 0
    Procedure1Clock.reset()  # clock
    frameN = -1
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
    # keep track of which components have finished
    Procedure1Components = [blackProc, greenProc, ProcTarget, ProcPicture]
    for thisComponent in Procedure1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Procedure1"-------
    while continueRoutine:
        # get current time
        t = Procedure1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *blackProc* updates
        if t >= 0.0 and blackProc.status == NOT_STARTED:
            # keep track of start time/frame for later
            blackProc.tStart = t
            blackProc.frameNStart = frameN  # exact frame index
            blackProc.setAutoDraw(True)
        frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blackProc.status == STARTED and t >= frameRemains:
            blackProc.setAutoDraw(False)
        
        # *greenProc* updates
        if t >= 0.0 and greenProc.status == NOT_STARTED:
            # keep track of start time/frame for later
            greenProc.tStart = t
            greenProc.frameNStart = frameN  # exact frame index
            greenProc.setAutoDraw(True)
        frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if greenProc.status == STARTED and t >= frameRemains:
            greenProc.setAutoDraw(False)
        
        # *ProcTarget* updates
        if t >= 0.0 and ProcTarget.status == NOT_STARTED:
            # keep track of start time/frame for later
            ProcTarget.tStart = t
            ProcTarget.frameNStart = frameN  # exact frame index
            ProcTarget.setAutoDraw(True)
        frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ProcTarget.status == STARTED and t >= frameRemains:
            ProcTarget.setAutoDraw(False)
        
        # *ProcPicture* updates
        if t >= 0.0 and ProcPicture.status == NOT_STARTED:
            # keep track of start time/frame for later
            ProcPicture.tStart = t
            ProcPicture.frameNStart = frameN  # exact frame index
            ProcPicture.setAutoDraw(True)
        frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ProcPicture.status == STARTED and t >= frameRemains:
            ProcPicture.setAutoDraw(False)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    
    
    # the Routine "Procedure1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "waitInterTrial"-------
    t = 0
    waitInterTrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # Send trial onset marker to LSL
    outlet.push_sample('n')
    whiteWaitInterTrial.setSize(pictureSize)
    # keep track of which components have finished
    waitInterTrialComponents = [blackWaitInterTrial, whiteWaitInterTrial]
    for thisComponent in waitInterTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "waitInterTrial"-------
    while continueRoutine:
        # get current time
        t = waitInterTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *blackWaitInterTrial* updates
        if t >= 0.0 and blackWaitInterTrial.status == NOT_STARTED:
            # keep track of start time/frame for later
            blackWaitInterTrial.tStart = t
            blackWaitInterTrial.frameNStart = frameN  # exact frame index
            blackWaitInterTrial.setAutoDraw(True)
        frameRemains = 0.0 + ITDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blackWaitInterTrial.status == STARTED and t >= frameRemains:
            blackWaitInterTrial.setAutoDraw(False)
        
        # *whiteWaitInterTrial* updates
        if t >= 0.0 and whiteWaitInterTrial.status == NOT_STARTED:
            # keep track of start time/frame for later
            whiteWaitInterTrial.tStart = t
            whiteWaitInterTrial.frameNStart = frameN  # exact frame index
            whiteWaitInterTrial.setAutoDraw(True)
        frameRemains = 0.0 + ITDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if whiteWaitInterTrial.status == STARTED and t >= frameRemains:
            whiteWaitInterTrial.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
        t = 0
        TrialListClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        index = index + 1
        
        TrialPicture.setSize(pictureSize)
        TrialPicture.setImage(Picture[index])
        keyPressTrial = event.BuilderKeyResponse()
        # Send trial onset marker to LSL
        #outlet.push_sample('t')
        outlet.push_sample(correctseth[index])
        PressedYet = 0
        # keep track of which components have finished
        TrialListComponents = [blackTrial, whiteTrial, TrialPicture, keyPressTrial]
        for thisComponent in TrialListComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "TrialList"-------
        while continueRoutine:
            # get current time
            t = TrialListClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *blackTrial* updates
            if t >= 0.0 and blackTrial.status == NOT_STARTED:
                # keep track of start time/frame for later
                blackTrial.tStart = t
                blackTrial.frameNStart = frameN  # exact frame index
                blackTrial.setAutoDraw(True)
            frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blackTrial.status == STARTED and t >= frameRemains:
                blackTrial.setAutoDraw(False)
            
            # *whiteTrial* updates
            if t >= 0.0 and whiteTrial.status == NOT_STARTED:
                # keep track of start time/frame for later
                whiteTrial.tStart = t
                whiteTrial.frameNStart = frameN  # exact frame index
                whiteTrial.setAutoDraw(True)
            frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if whiteTrial.status == STARTED and t >= frameRemains:
                whiteTrial.setAutoDraw(False)
            
            # *TrialPicture* updates
            if t >= 0.0 and TrialPicture.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialPicture.tStart = t
                TrialPicture.frameNStart = frameN  # exact frame index
                TrialPicture.setAutoDraw(True)
            frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if TrialPicture.status == STARTED and t >= frameRemains:
                TrialPicture.setAutoDraw(False)
            
            # *keyPressTrial* updates
            if t >= 0.0 and keyPressTrial.status == NOT_STARTED:
                # keep track of start time/frame for later
                keyPressTrial.tStart = t
                keyPressTrial.frameNStart = frameN  # exact frame index
                keyPressTrial.status = STARTED
                # keyboard checking is just starting
                keyPressTrial.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if keyPressTrial.status == STARTED and t >= frameRemains:
                keyPressTrial.status = FINISHED
            if keyPressTrial.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if keyPressTrial.keys == []:  # then this was the first keypress
                        keyPressTrial.keys = theseKeys[0]  # just the first key pressed
                        keyPressTrial.rt = keyPressTrial.clock.getTime()
            # Send trial onset marker to LSL
            #if ((keyPressTrial.keys) and (not PressedYet)):
            #    outlet.push_sample(str(keyPressTrial.keys)[0])
            #    PressedYet = 1
            
            if ((keyPressTrial.keys) and (not PressedYet)):
                if correctseth[index] == str(keyPressTrial.keys)[0]:
                    outlet.push_sample('1')
                    #print('correct')
                else:
                    outlet.push_sample('2')
                    #print('incorrect')
                PressedYet = 1
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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
        
        # check responses
        if keyPressTrial.keys in ['', [], None]:  # No response was made
            keyPressTrial.keys=None
        A1_trials.addData('keyPressTrial.keys',keyPressTrial.keys)
        if keyPressTrial.keys != None:  # we had a response
            A1_trials.addData('keyPressTrial.rt', keyPressTrial.rt)
        
        # the Routine "TrialList" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "InterTrial"-------
        t = 0
        InterTrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        whiteWaitInterTrial_2.setSize(pictureSize)
        # Send trial onset marker to LSL
        outlet.push_sample('n')
        
        
        # keep track of which components have finished
        InterTrialComponents = [blackWaitInterTrial_2, whiteWaitInterTrial_2]
        for thisComponent in InterTrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "InterTrial"-------
        while continueRoutine:
            # get current time
            t = InterTrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blackWaitInterTrial_2* updates
            if t >= 0.0 and blackWaitInterTrial_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                blackWaitInterTrial_2.tStart = t
                blackWaitInterTrial_2.frameNStart = frameN  # exact frame index
                blackWaitInterTrial_2.setAutoDraw(True)
            frameRemains = 0.0 + ITDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blackWaitInterTrial_2.status == STARTED and t >= frameRemains:
                blackWaitInterTrial_2.setAutoDraw(False)
            
            # *whiteWaitInterTrial_2* updates
            if t >= 0.0 and whiteWaitInterTrial_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                whiteWaitInterTrial_2.tStart = t
                whiteWaitInterTrial_2.frameNStart = frameN  # exact frame index
                whiteWaitInterTrial_2.setAutoDraw(True)
            frameRemains = 0.0 + ITDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if whiteWaitInterTrial_2.status == STARTED and t >= frameRemains:
                whiteWaitInterTrial_2.setAutoDraw(False)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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
        
        # the Routine "InterTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numTrials repeats of 'A1_trials'
    
    
    # ------Prepare to start Routine "Fixation"-------
    t = 0
    FixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    fixationImage.setSize(pictureSize)
    blockIdx = blockIdx + 1
    # keep track of which components have finished
    FixationComponents = [fixation, fixationImage]
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            fixation.setAutoDraw(False)
        
        # *fixationImage* updates
        if t >= 0.0 and fixationImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationImage.tStart = t
            fixationImage.frameNStart = frameN  # exact frame index
            fixationImage.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixationImage.status == STARTED and t >= frameRemains:
            fixationImage.setAutoDraw(False)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    
    thisExp.nextEntry()
    
# completed numBlocks repeats of 'A1_Blocks'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('e')
# keep track of which components have finished
endComponents = [polygon_end, end_text]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_end* updates
    if t >= 0.0 and polygon_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_end.tStart = t
        polygon_end.frameNStart = frameN  # exact frame index
        polygon_end.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_end.status == STARTED and t >= frameRemains:
        polygon_end.setAutoDraw(False)
    
    # *end_text* updates
    if t >= 0.0 and end_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text.tStart = t
        end_text.frameNStart = frameN  # exact frame index
        end_text.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if end_text.status == STARTED and t >= frameRemains:
        end_text.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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


# ------Prepare to start Routine "initiation_2"-------
t = 0
initiation_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# Read stimuli excel file
infile = './lib/listA2.xlsx'

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

# keep track of which components have finished
initiation_2Components = []
for thisComponent in initiation_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "initiation_2"-------
while continueRoutine:
    # get current time
    t = initiation_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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

# ------Prepare to start Routine "description_2"-------
t = 0
description_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyPressRun_2 = event.BuilderKeyResponse()
# keep track of which components have finished
description_2Components = [polygon_2, descriptionText_2, keyPressRun_2]
for thisComponent in description_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "description_2"-------
while continueRoutine:
    # get current time
    t = description_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if t >= 0.0 and polygon_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_2.tStart = t
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.setAutoDraw(True)
    
    # *descriptionText_2* updates
    if t >= 0.0 and descriptionText_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        descriptionText_2.tStart = t
        descriptionText_2.frameNStart = frameN  # exact frame index
        descriptionText_2.setAutoDraw(True)
    
    # *keyPressRun_2* updates
    if t >= 0.0 and keyPressRun_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyPressRun_2.tStart = t
        keyPressRun_2.frameNStart = frameN  # exact frame index
        keyPressRun_2.status = STARTED
        # keyboard checking is just starting
        keyPressRun_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if keyPressRun_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            keyPressRun_2.keys = theseKeys[-1]  # just the last key pressed
            keyPressRun_2.rt = keyPressRun_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in description_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "description_2"-------
for thisComponent in description_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyPressRun_2.keys in ['', [], None]:  # No response was made
    keyPressRun_2.keys=None
thisExp.addData('keyPressRun_2.keys',keyPressRun_2.keys)
if keyPressRun_2.keys != None:  # we had a response
    thisExp.addData('keyPressRun_2.rt', keyPressRun_2.rt)
thisExp.nextEntry()
# the Routine "description_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation10_2"-------
t = 0
Fixation10_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
fixationImage10_2.setSize(pictureSize)
# Send trial onset marker to LSL
outlet.push_sample('f')
# keep track of which components have finished
Fixation10_2Components = [fixation10_2, fixationImage10_2]
for thisComponent in Fixation10_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fixation10_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Fixation10_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation10_2* updates
    if t >= 0.0 and fixation10_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation10_2.tStart = t
        fixation10_2.frameNStart = frameN  # exact frame index
        fixation10_2.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixation10_2.status == STARTED and t >= frameRemains:
        fixation10_2.setAutoDraw(False)
    
    # *fixationImage10_2* updates
    if t >= 0.0 and fixationImage10_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixationImage10_2.tStart = t
        fixationImage10_2.frameNStart = frameN  # exact frame index
        fixationImage10_2.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixationImage10_2.status == STARTED and t >= frameRemains:
        fixationImage10_2.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fixation10_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fixation10_2"-------
for thisComponent in Fixation10_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


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
    t = 0
    Procedure1_2Clock.reset()  # clock
    frameN = -1
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
    # keep track of which components have finished
    Procedure1_2Components = [blackProc_2, greenProc_2, ProcTarget_2, ProcPicture_2]
    for thisComponent in Procedure1_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Procedure1_2"-------
    while continueRoutine:
        # get current time
        t = Procedure1_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *blackProc_2* updates
        if t >= 0.0 and blackProc_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            blackProc_2.tStart = t
            blackProc_2.frameNStart = frameN  # exact frame index
            blackProc_2.setAutoDraw(True)
        frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blackProc_2.status == STARTED and t >= frameRemains:
            blackProc_2.setAutoDraw(False)
        
        # *greenProc_2* updates
        if t >= 0.0 and greenProc_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            greenProc_2.tStart = t
            greenProc_2.frameNStart = frameN  # exact frame index
            greenProc_2.setAutoDraw(True)
        frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if greenProc_2.status == STARTED and t >= frameRemains:
            greenProc_2.setAutoDraw(False)
        
        # *ProcTarget_2* updates
        if t >= 0.0 and ProcTarget_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ProcTarget_2.tStart = t
            ProcTarget_2.frameNStart = frameN  # exact frame index
            ProcTarget_2.setAutoDraw(True)
        frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ProcTarget_2.status == STARTED and t >= frameRemains:
            ProcTarget_2.setAutoDraw(False)
        
        # *ProcPicture_2* updates
        if t >= 0.0 and ProcPicture_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ProcPicture_2.tStart = t
            ProcPicture_2.frameNStart = frameN  # exact frame index
            ProcPicture_2.setAutoDraw(True)
        frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ProcPicture_2.status == STARTED and t >= frameRemains:
            ProcPicture_2.setAutoDraw(False)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    
    
    # the Routine "Procedure1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "waitInterTrial_2"-------
    t = 0
    waitInterTrial_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # Send trial onset marker to LSL
    outlet.push_sample('n')
    whiteWaitInterTrial_3.setSize(pictureSize)
    # keep track of which components have finished
    waitInterTrial_2Components = [blackWaitInterTrial_3, whiteWaitInterTrial_3]
    for thisComponent in waitInterTrial_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "waitInterTrial_2"-------
    while continueRoutine:
        # get current time
        t = waitInterTrial_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *blackWaitInterTrial_3* updates
        if t >= 0.0 and blackWaitInterTrial_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            blackWaitInterTrial_3.tStart = t
            blackWaitInterTrial_3.frameNStart = frameN  # exact frame index
            blackWaitInterTrial_3.setAutoDraw(True)
        frameRemains = 0.0 + ITDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blackWaitInterTrial_3.status == STARTED and t >= frameRemains:
            blackWaitInterTrial_3.setAutoDraw(False)
        
        # *whiteWaitInterTrial_3* updates
        if t >= 0.0 and whiteWaitInterTrial_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            whiteWaitInterTrial_3.tStart = t
            whiteWaitInterTrial_3.frameNStart = frameN  # exact frame index
            whiteWaitInterTrial_3.setAutoDraw(True)
        frameRemains = 0.0 + ITDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
        if whiteWaitInterTrial_3.status == STARTED and t >= frameRemains:
            whiteWaitInterTrial_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
        t = 0
        TrialList_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        index = index + 1
        
        TrialPicture_2.setSize(pictureSize)
        TrialPicture_2.setImage(Picture[index])
        keyPressTrial_2 = event.BuilderKeyResponse()
        # Send trial onset marker to LSL
        #outlet.push_sample('t')
        outlet.push_sample(correctseth[index])
        PressedYet = 0
        # keep track of which components have finished
        TrialList_2Components = [blackTrial_2, whiteTrial_2, TrialPicture_2, keyPressTrial_2]
        for thisComponent in TrialList_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "TrialList_2"-------
        while continueRoutine:
            # get current time
            t = TrialList_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *blackTrial_2* updates
            if t >= 0.0 and blackTrial_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                blackTrial_2.tStart = t
                blackTrial_2.frameNStart = frameN  # exact frame index
                blackTrial_2.setAutoDraw(True)
            frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blackTrial_2.status == STARTED and t >= frameRemains:
                blackTrial_2.setAutoDraw(False)
            
            # *whiteTrial_2* updates
            if t >= 0.0 and whiteTrial_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                whiteTrial_2.tStart = t
                whiteTrial_2.frameNStart = frameN  # exact frame index
                whiteTrial_2.setAutoDraw(True)
            frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if whiteTrial_2.status == STARTED and t >= frameRemains:
                whiteTrial_2.setAutoDraw(False)
            
            # *TrialPicture_2* updates
            if t >= 0.0 and TrialPicture_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialPicture_2.tStart = t
                TrialPicture_2.frameNStart = frameN  # exact frame index
                TrialPicture_2.setAutoDraw(True)
            frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if TrialPicture_2.status == STARTED and t >= frameRemains:
                TrialPicture_2.setAutoDraw(False)
            
            # *keyPressTrial_2* updates
            if t >= 0.0 and keyPressTrial_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                keyPressTrial_2.tStart = t
                keyPressTrial_2.frameNStart = frameN  # exact frame index
                keyPressTrial_2.status = STARTED
                # keyboard checking is just starting
                keyPressTrial_2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + TrialDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if keyPressTrial_2.status == STARTED and t >= frameRemains:
                keyPressTrial_2.status = FINISHED
            if keyPressTrial_2.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if keyPressTrial_2.keys == []:  # then this was the first keypress
                        keyPressTrial_2.keys = theseKeys[0]  # just the first key pressed
                        keyPressTrial_2.rt = keyPressTrial_2.clock.getTime()
            # Send trial onset marker to LSL
            #if ((keyPressTrial.keys) and (not PressedYet)):
            #    outlet.push_sample(str(keyPressTrial.keys)[0])
            #    PressedYet = 1
            
            if ((keyPressTrial.keys) and (not PressedYet)):
                if correctseth[index] == str(keyPressTrial.keys)[0]:
                    outlet.push_sample('1')
                    #print('correct')
                else:
                    outlet.push_sample('2')
                    #print('incorrect')
                PressedYet = 1
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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
        
        # check responses
        if keyPressTrial_2.keys in ['', [], None]:  # No response was made
            keyPressTrial_2.keys=None
        A2_trials.addData('keyPressTrial_2.keys',keyPressTrial_2.keys)
        if keyPressTrial_2.keys != None:  # we had a response
            A2_trials.addData('keyPressTrial_2.rt', keyPressTrial_2.rt)
        
        # the Routine "TrialList_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "InterTrial_2"-------
        t = 0
        InterTrial_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        whiteWaitInterTrial_4.setSize(pictureSize)
        # Send trial onset marker to LSL
        outlet.push_sample('n')
        
        
        # keep track of which components have finished
        InterTrial_2Components = [blackWaitInterTrial_4, whiteWaitInterTrial_4]
        for thisComponent in InterTrial_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "InterTrial_2"-------
        while continueRoutine:
            # get current time
            t = InterTrial_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blackWaitInterTrial_4* updates
            if t >= 0.0 and blackWaitInterTrial_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                blackWaitInterTrial_4.tStart = t
                blackWaitInterTrial_4.frameNStart = frameN  # exact frame index
                blackWaitInterTrial_4.setAutoDraw(True)
            frameRemains = 0.0 + ITDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blackWaitInterTrial_4.status == STARTED and t >= frameRemains:
                blackWaitInterTrial_4.setAutoDraw(False)
            
            # *whiteWaitInterTrial_4* updates
            if t >= 0.0 and whiteWaitInterTrial_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                whiteWaitInterTrial_4.tStart = t
                whiteWaitInterTrial_4.frameNStart = frameN  # exact frame index
                whiteWaitInterTrial_4.setAutoDraw(True)
            frameRemains = 0.0 + ITDuration[index]- win.monitorFramePeriod * 0.75  # most of one frame period left
            if whiteWaitInterTrial_4.status == STARTED and t >= frameRemains:
                whiteWaitInterTrial_4.setAutoDraw(False)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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
        
        # the Routine "InterTrial_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numTrials repeats of 'A2_trials'
    
    
    # ------Prepare to start Routine "Fixation_2"-------
    t = 0
    Fixation_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    fixationImage_2.setSize(pictureSize)
    blockIdx = blockIdx + 1
    # keep track of which components have finished
    Fixation_2Components = [fixation_2, fixationImage_2]
    for thisComponent in Fixation_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Fixation_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Fixation_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_2* updates
        if t >= 0.0 and fixation_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_2.tStart = t
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_2.status == STARTED and t >= frameRemains:
            fixation_2.setAutoDraw(False)
        
        # *fixationImage_2* updates
        if t >= 0.0 and fixationImage_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationImage_2.tStart = t
            fixationImage_2.frameNStart = frameN  # exact frame index
            fixationImage_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixationImage_2.status == STARTED and t >= frameRemains:
            fixationImage_2.setAutoDraw(False)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    
    thisExp.nextEntry()
    
# completed numBlocks repeats of 'A2_Blocks'


# ------Prepare to start Routine "end_2"-------
t = 0
end_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('e')
# keep track of which components have finished
end_2Components = [polygon_end_2, end_text_2]
for thisComponent in end_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_end_2* updates
    if t >= 0.0 and polygon_end_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_end_2.tStart = t
        polygon_end_2.frameNStart = frameN  # exact frame index
        polygon_end_2.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_end_2.status == STARTED and t >= frameRemains:
        polygon_end_2.setAutoDraw(False)
    
    # *end_text_2* updates
    if t >= 0.0 and end_text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text_2.tStart = t
        end_text_2.frameNStart = frameN  # exact frame index
        end_text_2.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if end_text_2.status == STARTED and t >= frameRemains:
        end_text_2.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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


# ------Prepare to start Routine "desEyesOpen"-------
t = 0
desEyesOpenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyPressRun_3 = event.BuilderKeyResponse()
# keep track of which components have finished
desEyesOpenComponents = [polygon_3, descriptionText_3, keyPressRun_3]
for thisComponent in desEyesOpenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "desEyesOpen"-------
while continueRoutine:
    # get current time
    t = desEyesOpenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_3* updates
    if t >= 0.0 and polygon_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_3.tStart = t
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.setAutoDraw(True)
    
    # *descriptionText_3* updates
    if t >= 0.0 and descriptionText_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        descriptionText_3.tStart = t
        descriptionText_3.frameNStart = frameN  # exact frame index
        descriptionText_3.setAutoDraw(True)
    
    # *keyPressRun_3* updates
    if t >= 0.0 and keyPressRun_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyPressRun_3.tStart = t
        keyPressRun_3.frameNStart = frameN  # exact frame index
        keyPressRun_3.status = STARTED
        # keyboard checking is just starting
        keyPressRun_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if keyPressRun_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            keyPressRun_3.keys = theseKeys[-1]  # just the last key pressed
            keyPressRun_3.rt = keyPressRun_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in desEyesOpenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "desEyesOpen"-------
for thisComponent in desEyesOpenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyPressRun_3.keys in ['', [], None]:  # No response was made
    keyPressRun_3.keys=None
thisExp.addData('keyPressRun_3.keys',keyPressRun_3.keys)
if keyPressRun_3.keys != None:  # we had a response
    thisExp.addData('keyPressRun_3.rt', keyPressRun_3.rt)
thisExp.nextEntry()
# the Routine "desEyesOpen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation10_3"-------
t = 0
Fixation10_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
fixationImage10_3.setSize(pictureSize)
# Send trial onset marker to LSL
outlet.push_sample('f')
# keep track of which components have finished
Fixation10_3Components = [fixation10_3, fixationImage10_3]
for thisComponent in Fixation10_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fixation10_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Fixation10_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation10_3* updates
    if t >= 0.0 and fixation10_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation10_3.tStart = t
        fixation10_3.frameNStart = frameN  # exact frame index
        fixation10_3.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixation10_3.status == STARTED and t >= frameRemains:
        fixation10_3.setAutoDraw(False)
    
    # *fixationImage10_3* updates
    if t >= 0.0 and fixationImage10_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixationImage10_3.tStart = t
        fixationImage10_3.frameNStart = frameN  # exact frame index
        fixationImage10_3.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixationImage10_3.status == STARTED and t >= frameRemains:
        fixationImage10_3.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fixation10_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fixation10_3"-------
for thisComponent in Fixation10_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "EyesOpen"-------
t = 0
EyesOpenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(90.000000)
# update component parameters for each repeat
greenProc_3.setSize(greenSize)
ProcTarget_3.setSize(pictureSize)
ProcTarget_3.setImage('./stimuli/images/086.bmp')
ProcPicture_3.setSize(pictureSize)
ProcPicture_3.setImage('./stimuli/images/086.bmp')
# Send trial onset marker to LSL
outlet.push_sample('o')
# keep track of which components have finished
EyesOpenComponents = [blackProc_3, greenProc_3, ProcTarget_3, ProcPicture_3]
for thisComponent in EyesOpenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EyesOpen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EyesOpenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blackProc_3* updates
    if t >= 0.0 and blackProc_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        blackProc_3.tStart = t
        blackProc_3.frameNStart = frameN  # exact frame index
        blackProc_3.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blackProc_3.status == STARTED and t >= frameRemains:
        blackProc_3.setAutoDraw(False)
    
    # *greenProc_3* updates
    if t >= 0.0 and greenProc_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        greenProc_3.tStart = t
        greenProc_3.frameNStart = frameN  # exact frame index
        greenProc_3.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if greenProc_3.status == STARTED and t >= frameRemains:
        greenProc_3.setAutoDraw(False)
    
    # *ProcTarget_3* updates
    if t >= 0.0 and ProcTarget_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        ProcTarget_3.tStart = t
        ProcTarget_3.frameNStart = frameN  # exact frame index
        ProcTarget_3.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ProcTarget_3.status == STARTED and t >= frameRemains:
        ProcTarget_3.setAutoDraw(False)
    
    # *ProcPicture_3* updates
    if t >= 0.0 and ProcPicture_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        ProcPicture_3.tStart = t
        ProcPicture_3.frameNStart = frameN  # exact frame index
        ProcPicture_3.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ProcPicture_3.status == STARTED and t >= frameRemains:
        ProcPicture_3.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EyesOpenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EyesOpen"-------
for thisComponent in EyesOpenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "waitInterTrial_3"-------
t = 0
waitInterTrial_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('n')
whiteWaitInterTrial_5.setSize(pictureSize)
# keep track of which components have finished
waitInterTrial_3Components = [blackWaitInterTrial_5, whiteWaitInterTrial_5]
for thisComponent in waitInterTrial_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "waitInterTrial_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = waitInterTrial_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *blackWaitInterTrial_5* updates
    if t >= 0.0 and blackWaitInterTrial_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        blackWaitInterTrial_5.tStart = t
        blackWaitInterTrial_5.frameNStart = frameN  # exact frame index
        blackWaitInterTrial_5.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blackWaitInterTrial_5.status == STARTED and t >= frameRemains:
        blackWaitInterTrial_5.setAutoDraw(False)
    
    # *whiteWaitInterTrial_5* updates
    if t >= 0.0 and whiteWaitInterTrial_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        whiteWaitInterTrial_5.tStart = t
        whiteWaitInterTrial_5.frameNStart = frameN  # exact frame index
        whiteWaitInterTrial_5.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if whiteWaitInterTrial_5.status == STARTED and t >= frameRemains:
        whiteWaitInterTrial_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitInterTrial_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "waitInterTrial_3"-------
for thisComponent in waitInterTrial_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "desEyesClose"-------
t = 0
desEyesCloseClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyPressRun_4 = event.BuilderKeyResponse()
# keep track of which components have finished
desEyesCloseComponents = [polygon_4, descriptionText_4, keyPressRun_4]
for thisComponent in desEyesCloseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "desEyesClose"-------
while continueRoutine:
    # get current time
    t = desEyesCloseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_4* updates
    if t >= 0.0 and polygon_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_4.tStart = t
        polygon_4.frameNStart = frameN  # exact frame index
        polygon_4.setAutoDraw(True)
    
    # *descriptionText_4* updates
    if t >= 0.0 and descriptionText_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        descriptionText_4.tStart = t
        descriptionText_4.frameNStart = frameN  # exact frame index
        descriptionText_4.setAutoDraw(True)
    
    # *keyPressRun_4* updates
    if t >= 0.0 and keyPressRun_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyPressRun_4.tStart = t
        keyPressRun_4.frameNStart = frameN  # exact frame index
        keyPressRun_4.status = STARTED
        # keyboard checking is just starting
        keyPressRun_4.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if keyPressRun_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            keyPressRun_4.keys = theseKeys[-1]  # just the last key pressed
            keyPressRun_4.rt = keyPressRun_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in desEyesCloseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "desEyesClose"-------
for thisComponent in desEyesCloseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyPressRun_4.keys in ['', [], None]:  # No response was made
    keyPressRun_4.keys=None
thisExp.addData('keyPressRun_4.keys',keyPressRun_4.keys)
if keyPressRun_4.keys != None:  # we had a response
    thisExp.addData('keyPressRun_4.rt', keyPressRun_4.rt)
thisExp.nextEntry()
# the Routine "desEyesClose" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation10_4"-------
t = 0
Fixation10_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
fixationImage10_4.setSize(pictureSize)
# Send trial onset marker to LSL
outlet.push_sample('f')
# keep track of which components have finished
Fixation10_4Components = [fixation10_4, fixationImage10_4]
for thisComponent in Fixation10_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fixation10_4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Fixation10_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation10_4* updates
    if t >= 0.0 and fixation10_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation10_4.tStart = t
        fixation10_4.frameNStart = frameN  # exact frame index
        fixation10_4.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixation10_4.status == STARTED and t >= frameRemains:
        fixation10_4.setAutoDraw(False)
    
    # *fixationImage10_4* updates
    if t >= 0.0 and fixationImage10_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixationImage10_4.tStart = t
        fixationImage10_4.frameNStart = frameN  # exact frame index
        fixationImage10_4.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixationImage10_4.status == STARTED and t >= frameRemains:
        fixationImage10_4.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fixation10_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fixation10_4"-------
for thisComponent in Fixation10_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "EyesClose"-------
t = 0
EyesCloseClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(90.000000)
# update component parameters for each repeat
greenProc_4.setSize(greenSize)
ProcTarget_4.setSize(pictureSize)
ProcTarget_4.setImage('./stimuli/images/086.bmp')
ProcPicture_4.setSize(pictureSize)
ProcPicture_4.setImage('./stimuli/images/086.bmp')
# Send trial onset marker to LSL
outlet.push_sample('c')
# keep track of which components have finished
EyesCloseComponents = [blackProc_4, greenProc_4, ProcTarget_4, ProcPicture_4]
for thisComponent in EyesCloseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EyesClose"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EyesCloseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blackProc_4* updates
    if t >= 0.0 and blackProc_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        blackProc_4.tStart = t
        blackProc_4.frameNStart = frameN  # exact frame index
        blackProc_4.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blackProc_4.status == STARTED and t >= frameRemains:
        blackProc_4.setAutoDraw(False)
    
    # *greenProc_4* updates
    if t >= 0.0 and greenProc_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        greenProc_4.tStart = t
        greenProc_4.frameNStart = frameN  # exact frame index
        greenProc_4.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if greenProc_4.status == STARTED and t >= frameRemains:
        greenProc_4.setAutoDraw(False)
    
    # *ProcTarget_4* updates
    if t >= 0.0 and ProcTarget_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        ProcTarget_4.tStart = t
        ProcTarget_4.frameNStart = frameN  # exact frame index
        ProcTarget_4.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ProcTarget_4.status == STARTED and t >= frameRemains:
        ProcTarget_4.setAutoDraw(False)
    
    # *ProcPicture_4* updates
    if t >= 0.0 and ProcPicture_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        ProcPicture_4.tStart = t
        ProcPicture_4.frameNStart = frameN  # exact frame index
        ProcPicture_4.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ProcPicture_4.status == STARTED and t >= frameRemains:
        ProcPicture_4.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EyesCloseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EyesClose"-------
for thisComponent in EyesCloseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "waitInterTrial_4"-------
t = 0
waitInterTrial_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('n')
whiteWaitInterTrial_6.setSize(pictureSize)
# keep track of which components have finished
waitInterTrial_4Components = [blackWaitInterTrial_6, whiteWaitInterTrial_6]
for thisComponent in waitInterTrial_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "waitInterTrial_4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = waitInterTrial_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *blackWaitInterTrial_6* updates
    if t >= 0.0 and blackWaitInterTrial_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        blackWaitInterTrial_6.tStart = t
        blackWaitInterTrial_6.frameNStart = frameN  # exact frame index
        blackWaitInterTrial_6.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blackWaitInterTrial_6.status == STARTED and t >= frameRemains:
        blackWaitInterTrial_6.setAutoDraw(False)
    
    # *whiteWaitInterTrial_6* updates
    if t >= 0.0 and whiteWaitInterTrial_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        whiteWaitInterTrial_6.tStart = t
        whiteWaitInterTrial_6.frameNStart = frameN  # exact frame index
        whiteWaitInterTrial_6.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if whiteWaitInterTrial_6.status == STARTED and t >= frameRemains:
        whiteWaitInterTrial_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitInterTrial_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "waitInterTrial_4"-------
for thisComponent in waitInterTrial_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "end_3"-------
t = 0
end_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('e')

# keep track of which components have finished
end_3Components = [polygon_end_3, end_text_3]
for thisComponent in end_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_end_3* updates
    if t >= 0.0 and polygon_end_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_end_3.tStart = t
        polygon_end_3.frameNStart = frameN  # exact frame index
        polygon_end_3.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_end_3.status == STARTED and t >= frameRemains:
        polygon_end_3.setAutoDraw(False)
    
    # *end_text_3* updates
    if t >= 0.0 and end_text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text_3.tStart = t
        end_text_3.frameNStart = frameN  # exact frame index
        end_text_3.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if end_text_3.status == STARTED and t >= frameRemains:
        end_text_3.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_3"-------
for thisComponent in end_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
child.sendline('\r')



























# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
