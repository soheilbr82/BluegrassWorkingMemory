#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on October 07, 2019, at 10:18
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
psychopyVersion = '3.2.3'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
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
    originPath='D:\\Projects\\Psychopy_BluegrassWMPlatform\\For_Testing_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

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

# Initialize components for Routine "initiation_practice"
initiation_practiceClock = core.Clock()

# Initialize components for Routine "description_practice_1"
description_practice_1Clock = core.Clock()
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText_5 = visual.TextStim(win=win, name='descriptionText_5',
    text='Practice for the Right-handed\n\nPlease determine whether each image matches one of the images shown with a green border. \n\nKeep your left and right pointer fingers on the A and L keys at all times\n\nPress SPACEBAR to continue',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyPressRun_5 = keyboard.Keyboard()

# Initialize components for Routine "initiation"
initiationClock = core.Clock()

# Initialize components for Routine "desEyesOpen_1"
desEyesOpen_1Clock = core.Clock()
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText_3 = visual.TextStim(win=win, name='descriptionText_3',
    text='Eyes open for 1.5 minute\nPlease stare at fixation point\n\n\n\n\nPress SPACEBAR to continue',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyPressRun_3 = keyboard.Keyboard()

# Initialize components for Routine "desEyesOpen_3"
desEyesOpen_3Clock = core.Clock()
polygon_9 = visual.Rect(
    win=win, name='polygon_9',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText_9 = visual.TextStim(win=win, name='descriptionText_9',
    text='Try to be as still as possible\n\nWe will let you know as soon as minute is up\n\n\n\n\nPress SPACEBAR to continue',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyPressRun_9 = keyboard.Keyboard()

# Initialize components for Routine "description_A1_1"
description_A1_1Clock = core.Clock()
polygon_12 = visual.Rect(
    win=win, name='polygon_12',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText_12 = visual.TextStim(win=win, name='descriptionText_12',
    text='Round 1\n\nPlease determine whether each image matches one of the images shown with a green border. \n\n press the L key to choose match, and press the A key to choose “non match”.\n\nKeep your left and right pointer fingers on the A and L at all time\n\n\nPress SPACEBAR to continue',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyPressRun_12 = keyboard.Keyboard()

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
    depth=-3.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='2 . .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='1 .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

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
    opacity=1, depth=-1.0, interpolate=True)
whiteWaitInterTrial = visual.ImageStim(
    win=win,
    name='whiteWaitInterTrial', 
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
    win=win,
    name='TrialPicture', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
keyPressTrial = keyboard.Keyboard()

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
    depth=-3.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='2 . .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='1 .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

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
    opacity=1, depth=-1.0, interpolate=True)
whiteWaitInterTrial_3 = visual.ImageStim(
    win=win,
    name='whiteWaitInterTrial_3', 
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
    win=win,
    name='TrialPicture_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
keyPressTrial_2 = keyboard.Keyboard()

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

# ------Prepare to start Routine "initiation_practice"-------
# update component parameters for each repeat


# Add random and excel library
import random, xlrd, os, sys
sys.path.append('./lib/')
pictureSize=(0.75,1)
greenSize=(1.6,1.2)


# Read stimuli excel file
infile = './lib/listA3_Righty.xlsx'

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
initiation_practiceComponents = []
for thisComponent in initiation_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initiation_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "initiation_practice"-------
while continueRoutine:
    # get current time
    t = initiation_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initiation_practiceClock)
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
    for thisComponent in initiation_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initiation_practice"-------
for thisComponent in initiation_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initiation_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "description_practice_1"-------
# update component parameters for each repeat
keyPressRun_5.keys = []
keyPressRun_5.rt = []
# keep track of which components have finished
description_practice_1Components = [polygon_5, descriptionText_5, keyPressRun_5]
for thisComponent in description_practice_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
description_practice_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "description_practice_1"-------
while continueRoutine:
    # get current time
    t = description_practice_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=description_practice_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_5* updates
    if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_5.frameNStart = frameN  # exact frame index
        polygon_5.tStart = t  # local t and not account for scr refresh
        polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
        polygon_5.setAutoDraw(True)
    
    # *descriptionText_5* updates
    if descriptionText_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionText_5.frameNStart = frameN  # exact frame index
        descriptionText_5.tStart = t  # local t and not account for scr refresh
        descriptionText_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionText_5, 'tStartRefresh')  # time at next scr refresh
        descriptionText_5.setAutoDraw(True)
    
    # *keyPressRun_5* updates
    if keyPressRun_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyPressRun_5.frameNStart = frameN  # exact frame index
        keyPressRun_5.tStart = t  # local t and not account for scr refresh
        keyPressRun_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyPressRun_5, 'tStartRefresh')  # time at next scr refresh
        keyPressRun_5.status = STARTED
        # keyboard checking is just starting
        keyPressRun_5.clock.reset()  # now t=0
        keyPressRun_5.clearEvents(eventType='keyboard')
    if keyPressRun_5.status == STARTED:
        theseKeys = keyPressRun_5.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyPressRun_5.keys = theseKeys.name  # just the last key pressed
            keyPressRun_5.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in description_practice_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "description_practice_1"-------
for thisComponent in description_practice_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_5.started', polygon_5.tStartRefresh)
thisExp.addData('polygon_5.stopped', polygon_5.tStopRefresh)
thisExp.addData('descriptionText_5.started', descriptionText_5.tStartRefresh)
thisExp.addData('descriptionText_5.stopped', descriptionText_5.tStopRefresh)
# check responses
if keyPressRun_5.keys in ['', [], None]:  # No response was made
    keyPressRun_5.keys = None
thisExp.addData('keyPressRun_5.keys',keyPressRun_5.keys)
if keyPressRun_5.keys != None:  # we had a response
    thisExp.addData('keyPressRun_5.rt', keyPressRun_5.rt)
thisExp.addData('keyPressRun_5.started', keyPressRun_5.tStart)
thisExp.addData('keyPressRun_5.stopped', keyPressRun_5.tStop)
thisExp.nextEntry()
# the Routine "description_practice_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "initiation"-------
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
child =  winpexpect.winspawn('%s %s\%s_%s.xdf \'name="Keyboard"\'' % (Labrecorder,Dataset,subjectID,currentTime))



# Fix random seed
random.seed()
# Read stimuli excel file
infile = './lib/listA1_Righty.xlsx'
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
continueRoutine = True

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

# ------Prepare to start Routine "desEyesOpen_1"-------
# update component parameters for each repeat
keyPressRun_3.keys = []
keyPressRun_3.rt = []
# keep track of which components have finished
desEyesOpen_1Components = [polygon_3, descriptionText_3, keyPressRun_3]
for thisComponent in desEyesOpen_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
desEyesOpen_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "desEyesOpen_1"-------
while continueRoutine:
    # get current time
    t = desEyesOpen_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=desEyesOpen_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_3* updates
    if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.tStart = t  # local t and not account for scr refresh
        polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *descriptionText_3* updates
    if descriptionText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionText_3.frameNStart = frameN  # exact frame index
        descriptionText_3.tStart = t  # local t and not account for scr refresh
        descriptionText_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionText_3, 'tStartRefresh')  # time at next scr refresh
        descriptionText_3.setAutoDraw(True)
    
    # *keyPressRun_3* updates
    if keyPressRun_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyPressRun_3.frameNStart = frameN  # exact frame index
        keyPressRun_3.tStart = t  # local t and not account for scr refresh
        keyPressRun_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyPressRun_3, 'tStartRefresh')  # time at next scr refresh
        keyPressRun_3.status = STARTED
        # keyboard checking is just starting
        keyPressRun_3.clock.reset()  # now t=0
        keyPressRun_3.clearEvents(eventType='keyboard')
    if keyPressRun_3.status == STARTED:
        theseKeys = keyPressRun_3.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyPressRun_3.keys = theseKeys.name  # just the last key pressed
            keyPressRun_3.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in desEyesOpen_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "desEyesOpen_1"-------
for thisComponent in desEyesOpen_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_3.started', polygon_3.tStartRefresh)
thisExp.addData('polygon_3.stopped', polygon_3.tStopRefresh)
thisExp.addData('descriptionText_3.started', descriptionText_3.tStartRefresh)
thisExp.addData('descriptionText_3.stopped', descriptionText_3.tStopRefresh)
# check responses
if keyPressRun_3.keys in ['', [], None]:  # No response was made
    keyPressRun_3.keys = None
thisExp.addData('keyPressRun_3.keys',keyPressRun_3.keys)
if keyPressRun_3.keys != None:  # we had a response
    thisExp.addData('keyPressRun_3.rt', keyPressRun_3.rt)
thisExp.addData('keyPressRun_3.started', keyPressRun_3.tStart)
thisExp.addData('keyPressRun_3.stopped', keyPressRun_3.tStop)
thisExp.nextEntry()
# the Routine "desEyesOpen_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "desEyesOpen_3"-------
# update component parameters for each repeat
keyPressRun_9.keys = []
keyPressRun_9.rt = []
# keep track of which components have finished
desEyesOpen_3Components = [polygon_9, descriptionText_9, keyPressRun_9]
for thisComponent in desEyesOpen_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
desEyesOpen_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "desEyesOpen_3"-------
while continueRoutine:
    # get current time
    t = desEyesOpen_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=desEyesOpen_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_9* updates
    if polygon_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_9.frameNStart = frameN  # exact frame index
        polygon_9.tStart = t  # local t and not account for scr refresh
        polygon_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
        polygon_9.setAutoDraw(True)
    
    # *descriptionText_9* updates
    if descriptionText_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionText_9.frameNStart = frameN  # exact frame index
        descriptionText_9.tStart = t  # local t and not account for scr refresh
        descriptionText_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionText_9, 'tStartRefresh')  # time at next scr refresh
        descriptionText_9.setAutoDraw(True)
    
    # *keyPressRun_9* updates
    if keyPressRun_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyPressRun_9.frameNStart = frameN  # exact frame index
        keyPressRun_9.tStart = t  # local t and not account for scr refresh
        keyPressRun_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyPressRun_9, 'tStartRefresh')  # time at next scr refresh
        keyPressRun_9.status = STARTED
        # keyboard checking is just starting
        keyPressRun_9.clock.reset()  # now t=0
        keyPressRun_9.clearEvents(eventType='keyboard')
    if keyPressRun_9.status == STARTED:
        theseKeys = keyPressRun_9.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyPressRun_9.keys = theseKeys.name  # just the last key pressed
            keyPressRun_9.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in desEyesOpen_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "desEyesOpen_3"-------
for thisComponent in desEyesOpen_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_9.started', polygon_9.tStartRefresh)
thisExp.addData('polygon_9.stopped', polygon_9.tStopRefresh)
thisExp.addData('descriptionText_9.started', descriptionText_9.tStartRefresh)
thisExp.addData('descriptionText_9.stopped', descriptionText_9.tStopRefresh)
# check responses
if keyPressRun_9.keys in ['', [], None]:  # No response was made
    keyPressRun_9.keys = None
thisExp.addData('keyPressRun_9.keys',keyPressRun_9.keys)
if keyPressRun_9.keys != None:  # we had a response
    thisExp.addData('keyPressRun_9.rt', keyPressRun_9.rt)
thisExp.addData('keyPressRun_9.started', keyPressRun_9.tStart)
thisExp.addData('keyPressRun_9.stopped', keyPressRun_9.tStop)
thisExp.nextEntry()
# the Routine "desEyesOpen_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "description_A1_1"-------
# update component parameters for each repeat
keyPressRun_12.keys = []
keyPressRun_12.rt = []
# keep track of which components have finished
description_A1_1Components = [polygon_12, descriptionText_12, keyPressRun_12]
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
continueRoutine = True

# -------Run Routine "description_A1_1"-------
while continueRoutine:
    # get current time
    t = description_A1_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=description_A1_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_12* updates
    if polygon_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_12.frameNStart = frameN  # exact frame index
        polygon_12.tStart = t  # local t and not account for scr refresh
        polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
        polygon_12.setAutoDraw(True)
    
    # *descriptionText_12* updates
    if descriptionText_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionText_12.frameNStart = frameN  # exact frame index
        descriptionText_12.tStart = t  # local t and not account for scr refresh
        descriptionText_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionText_12, 'tStartRefresh')  # time at next scr refresh
        descriptionText_12.setAutoDraw(True)
    
    # *keyPressRun_12* updates
    if keyPressRun_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyPressRun_12.frameNStart = frameN  # exact frame index
        keyPressRun_12.tStart = t  # local t and not account for scr refresh
        keyPressRun_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyPressRun_12, 'tStartRefresh')  # time at next scr refresh
        keyPressRun_12.status = STARTED
        # keyboard checking is just starting
        keyPressRun_12.clock.reset()  # now t=0
        keyPressRun_12.clearEvents(eventType='keyboard')
    if keyPressRun_12.status == STARTED:
        theseKeys = keyPressRun_12.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyPressRun_12.keys = theseKeys.name  # just the last key pressed
            keyPressRun_12.rt = theseKeys.rt
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
thisExp.addData('polygon_12.started', polygon_12.tStartRefresh)
thisExp.addData('polygon_12.stopped', polygon_12.tStopRefresh)
thisExp.addData('descriptionText_12.started', descriptionText_12.tStartRefresh)
thisExp.addData('descriptionText_12.stopped', descriptionText_12.tStopRefresh)
# check responses
if keyPressRun_12.keys in ['', [], None]:  # No response was made
    keyPressRun_12.keys = None
thisExp.addData('keyPressRun_12.keys',keyPressRun_12.keys)
if keyPressRun_12.keys != None:  # we had a response
    thisExp.addData('keyPressRun_12.rt', keyPressRun_12.rt)
thisExp.addData('keyPressRun_12.started', keyPressRun_12.tStart)
thisExp.addData('keyPressRun_12.stopped', keyPressRun_12.tStop)
thisExp.nextEntry()
# the Routine "description_A1_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation10"-------
routineTimer.add(10.000000)
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
continueRoutine = True

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
        if tThisFlipGlobal > fixation10.tStartRefresh + 10.0-frameTolerance:
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
        if tThisFlipGlobal > fixationImage10.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            fixationImage10.tStop = t  # not accounting for scr refresh
            fixationImage10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixationImage10, 'tStopRefresh')  # time at next scr refresh
            fixationImage10.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 7.0-frameTolerance:
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
    if text_2.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
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
    if text_3.status == NOT_STARTED and tThisFlip >= 9.0-frameTolerance:
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
    continueRoutine = True
    
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
    # update component parameters for each repeat
    # Send trial onset marker to LSL
    outlet.push_sample('n')
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
    continueRoutine = True
    
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
        # update component parameters for each repeat
        index = index + 1
        
        TrialPicture.setSize(pictureSize)
        TrialPicture.setImage(Picture[index])
        keyPressTrial.keys = []
        keyPressTrial.rt = []
        # Send trial onset marker to LSL
        #outlet.push_sample('t')
        outlet.push_sample(correctseth[index])
        PressedYet = 0
        # keep track of which components have finished
        TrialListComponents = [blackTrial, whiteTrial, TrialPicture, keyPressTrial]
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
        continueRoutine = True
        
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
            
            # *keyPressTrial* updates
            if keyPressTrial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyPressTrial.frameNStart = frameN  # exact frame index
                keyPressTrial.tStart = t  # local t and not account for scr refresh
                keyPressTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyPressTrial, 'tStartRefresh')  # time at next scr refresh
                keyPressTrial.status = STARTED
                # keyboard checking is just starting
                keyPressTrial.clock.reset()  # now t=0
                keyPressTrial.clearEvents(eventType='keyboard')
            if keyPressTrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyPressTrial.tStartRefresh + TrialDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    keyPressTrial.tStop = t  # not accounting for scr refresh
                    keyPressTrial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(keyPressTrial, 'tStopRefresh')  # time at next scr refresh
                    keyPressTrial.status = FINISHED
            if keyPressTrial.status == STARTED:
                theseKeys = keyPressTrial.getKeys(keyList=None, waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if keyPressTrial.keys == []:  # then this was the first keypress
                        keyPressTrial.keys = theseKeys.name  # just the first key pressed
                        keyPressTrial.rt = theseKeys.rt
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
        if keyPressTrial.keys in ['', [], None]:  # No response was made
            keyPressTrial.keys = None
        A1_trials.addData('keyPressTrial.keys',keyPressTrial.keys)
        if keyPressTrial.keys != None:  # we had a response
            A1_trials.addData('keyPressTrial.rt', keyPressTrial.rt)
        A1_trials.addData('keyPressTrial.started', keyPressTrial.tStart)
        A1_trials.addData('keyPressTrial.stopped', keyPressTrial.tStop)
        # the Routine "TrialList" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "InterTrial"-------
        # update component parameters for each repeat
        whiteWaitInterTrial_2.setSize(pictureSize)
        # Send trial onset marker to LSL
        outlet.push_sample('n')
        
        
        # keep track of which components have finished
        InterTrialComponents = [blackWaitInterTrial_2, whiteWaitInterTrial_2]
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
        continueRoutine = True
        
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
                if tThisFlipGlobal > blackWaitInterTrial_2.tStartRefresh + ITDuration[index]-frameTolerance:
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
                if tThisFlipGlobal > whiteWaitInterTrial_2.tStartRefresh + ITDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    whiteWaitInterTrial_2.tStop = t  # not accounting for scr refresh
                    whiteWaitInterTrial_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(whiteWaitInterTrial_2, 'tStopRefresh')  # time at next scr refresh
                    whiteWaitInterTrial_2.setAutoDraw(False)
            
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
        # the Routine "InterTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numTrials repeats of 'A1_trials'
    
    
    # ------Prepare to start Routine "Fixation"-------
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
    continueRoutine = True
    
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
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('e')
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
continueRoutine = True

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
# update component parameters for each repeat

# Read stimuli excel file
infile = './lib/listA2_Lefty.xlsx'

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
continueRoutine = True

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
# update component parameters for each repeat
keyPressRun_15.keys = []
keyPressRun_15.rt = []
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
continueRoutine = True

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
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyPressRun_15.keys = theseKeys.name  # just the last key pressed
            keyPressRun_15.rt = theseKeys.rt
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
routineTimer.add(10.000000)
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
continueRoutine = True

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
        if tThisFlipGlobal > fixation10.tStartRefresh + 10.0-frameTolerance:
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
        if tThisFlipGlobal > fixationImage10.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            fixationImage10.tStop = t  # not accounting for scr refresh
            fixationImage10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixationImage10, 'tStopRefresh')  # time at next scr refresh
            fixationImage10.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 7.0-frameTolerance:
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
    if text_2.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
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
    if text_3.status == NOT_STARTED and tThisFlip >= 9.0-frameTolerance:
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
A2_Blocks = data.TrialHandler(nReps=2, method='sequential', 
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
    continueRoutine = True
    
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
    # update component parameters for each repeat
    # Send trial onset marker to LSL
    outlet.push_sample('n')
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
    continueRoutine = True
    
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
        # update component parameters for each repeat
        index = index + 1
        
        TrialPicture_2.setSize(pictureSize)
        TrialPicture_2.setImage(Picture[index])
        keyPressTrial_2.keys = []
        keyPressTrial_2.rt = []
        # Send trial onset marker to LSL
        #outlet.push_sample('t')
        outlet.push_sample(correctseth[index])
        PressedYet = 0
        # keep track of which components have finished
        TrialList_2Components = [blackTrial_2, whiteTrial_2, TrialPicture_2, keyPressTrial_2]
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
        continueRoutine = True
        
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
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if keyPressTrial_2.keys == []:  # then this was the first keypress
                        keyPressTrial_2.keys = theseKeys.name  # just the first key pressed
                        keyPressTrial_2.rt = theseKeys.rt
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
        # the Routine "TrialList_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "InterTrial_2"-------
        # update component parameters for each repeat
        whiteWaitInterTrial_4.setSize(pictureSize)
        # Send trial onset marker to LSL
        outlet.push_sample('n')
        
        
        # keep track of which components have finished
        InterTrial_2Components = [blackWaitInterTrial_4, whiteWaitInterTrial_4]
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
        continueRoutine = True
        
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
                if tThisFlipGlobal > blackWaitInterTrial_4.tStartRefresh + ITDuration[index]-frameTolerance:
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
                if tThisFlipGlobal > whiteWaitInterTrial_4.tStartRefresh + ITDuration[index]-frameTolerance:
                    # keep track of stop time/frame for later
                    whiteWaitInterTrial_4.tStop = t  # not accounting for scr refresh
                    whiteWaitInterTrial_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(whiteWaitInterTrial_4, 'tStopRefresh')  # time at next scr refresh
                    whiteWaitInterTrial_4.setAutoDraw(False)
            
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
        # the Routine "InterTrial_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numTrials repeats of 'A2_trials'
    
    
    # ------Prepare to start Routine "Fixation_2"-------
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
    continueRoutine = True
    
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
    
# completed 2 repeats of 'A2_Blocks'


# ------Prepare to start Routine "end_2"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('e')
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
continueRoutine = True

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
child.sendline('\r')

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
