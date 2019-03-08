#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.1),
    on March 08, 2019, at 15:19
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
    originPath='D:\\Projects\\BluegrassWMPlatform_PsychopyV2\\BluegrassWM_A2_lastrun.py',
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
# Add random and excel library
import random, xlrd, os, sys
sys.path.append('./lib/')

# Open LabRecorder
#os.startfile(".\lib\LabRecorder\LabRecorder.exe")




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
import subprocess, sys, os
#os.system("start /B start cmd.exe @cmd /k .\lib\LabRecorder\LabRecorderCLI.exe .\Dataset\'currentTime'.xdf 'type=EEG'")
os.system("start /B start cmd.exe @cmd /k %s %s\%s_%s 'type=EEG'" % (Labrecorder, Dataset, currentTime,subjectID))







# Fix random seed
random.seed()
# Read stimuli excel file
infile = './lib/listA2.xlsx'
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
    text='Please determine whether each image matches one of the images shown with a green border. \nIf it matches,\nplease quickly press the A (L) key.\nIf it does not,\nplease quickly press the L (A) key.\n\nIf a cross (+) appears appears,\nplease quickly press both keys.\n\nPRESS THE SPACEBAR WHEN READY',
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
        win.callOnFlip(keyPressRun.clock.reset)  # t=0 on next screen flip
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
TrialListIteration = data.TrialHandler(nReps=numBlocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='TrialListIteration')
thisExp.addLoop(TrialListIteration)  # add the loop to the experiment
thisTrialListIteration = TrialListIteration.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialListIteration.rgb)
if thisTrialListIteration != None:
    for paramName in thisTrialListIteration:
        exec('{} = thisTrialListIteration[paramName]'.format(paramName))

for thisTrialListIteration in TrialListIteration:
    currentLoop = TrialListIteration
    # abbreviate parameter names if possible (e.g. rgb = thisTrialListIteration.rgb)
    if thisTrialListIteration != None:
        for paramName in thisTrialListIteration:
            exec('{} = thisTrialListIteration[paramName]'.format(paramName))
    
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
    trials = data.TrialHandler(nReps=numTrials, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
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
        trials.addData('keyPressTrial.keys',keyPressTrial.keys)
        if keyPressTrial.keys != None:  # we had a response
            trials.addData('keyPressTrial.rt', keyPressTrial.rt)
        
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
        
    # completed numTrials repeats of 'trials'
    
    
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
    
# completed numBlocks repeats of 'TrialListIteration'


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










# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
