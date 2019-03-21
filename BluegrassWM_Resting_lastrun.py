#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.1),
    on March 21, 2019, at 18:03
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
    originPath='D:\\Projects\\BluegrassWMPlatform_Psychopy\\BluegrassWM_Resting_lastrun.py',
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
import subprocess, sys, os, winpexpect, time
#os.system("start /B start cmd.exe @cmd /k .\lib\LabRecorder\LabRecorderCLI.exe .\Dataset\'currentTime'.xdf 'type=EEG'")
#os.system("start /B start cmd.exe @cmd /k %s %s\%s_%s 'type=EEG'" % (Labrecorder, Dataset, currentTime,subjectID))
child =  winpexpect.winspawn('%s %s\%s_%s \'name="Keyboard"\'' % (Labrecorder,Dataset,currentTime,subjectID))



# Fix random seed
random.seed()


pictureSize=(0.75,1)
greenSize=(1.6,1.2)




# Initialize components for Routine "description1"
description1Clock = core.Clock()
polygon1 = visual.Rect(
    win=win, name='polygon1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText1 = visual.TextStim(win=win, name='descriptionText1',
    text='Eyes open for one minute\nPlease stare at fixation point\n\nTry not to blink during this time\n\nTry to be as still as possible\n\nWe will come in as soon as minute is up',
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
    text='1 . .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "EyesOpen"
EyesOpenClock = core.Clock()
blackProc = visual.Rect(
    win=win, name='blackProc',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
greenProc = visual.Rect(
    win=win, name='greenProc',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
ProcTarget = visual.ImageStim(
    win=win, name='ProcTarget',
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
ProcPicture = visual.ImageStim(
    win=win, name='ProcPicture',
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


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

# Initialize components for Routine "description2"
description2Clock = core.Clock()
polygon2 = visual.Rect(
    win=win, name='polygon2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
descriptionText2 = visual.TextStim(win=win, name='descriptionText2',
    text='Eyes close for one minute\n\nTry not to blink during this time\n\nTry to be as still as possible\n\nWe will come in as soon as minute is up',
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
    text='1 . .',
    font='Arial',
    pos=(0, -0.7), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "EyesClose"
EyesCloseClock = core.Clock()
blackProc_2 = visual.Rect(
    win=win, name='blackProc_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
greenProc_2 = visual.Rect(
    win=win, name='greenProc_2',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
ProcTarget_2 = visual.ImageStim(
    win=win, name='ProcTarget_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


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

# ------Prepare to start Routine "description1"-------
t = 0
description1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyPressRun1 = event.BuilderKeyResponse()
# keep track of which components have finished
description1Components = [polygon1, descriptionText1, keyPressRun1]
for thisComponent in description1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "description1"-------
while continueRoutine:
    # get current time
    t = description1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon1* updates
    if t >= 0.0 and polygon1.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon1.tStart = t
        polygon1.frameNStart = frameN  # exact frame index
        polygon1.setAutoDraw(True)
    
    # *descriptionText1* updates
    if t >= 0.0 and descriptionText1.status == NOT_STARTED:
        # keep track of start time/frame for later
        descriptionText1.tStart = t
        descriptionText1.frameNStart = frameN  # exact frame index
        descriptionText1.setAutoDraw(True)
    
    # *keyPressRun1* updates
    if t >= 0.0 and keyPressRun1.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyPressRun1.tStart = t
        keyPressRun1.frameNStart = frameN  # exact frame index
        keyPressRun1.status = STARTED
        # keyboard checking is just starting
        keyPressRun1.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if keyPressRun1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            keyPressRun1.keys = theseKeys[-1]  # just the last key pressed
            keyPressRun1.rt = keyPressRun1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in description1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "description1"-------
for thisComponent in description1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyPressRun1.keys in ['', [], None]:  # No response was made
    keyPressRun1.keys=None
thisExp.addData('keyPressRun1.keys',keyPressRun1.keys)
if keyPressRun1.keys != None:  # we had a response
    thisExp.addData('keyPressRun1.rt', keyPressRun1.rt)
thisExp.nextEntry()
# the Routine "description1" was not non-slip safe, so reset the non-slip timer
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
Fixation10Components = [fixation10, fixationImage10, text, text_2, text_3]
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
    
    # *text* updates
    if t >= 7.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 7.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # *text_2* updates
    if t >= 8.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 8.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
    # *text_3* updates
    if t >= 9.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    frameRemains = 9.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_3.status == STARTED and t >= frameRemains:
        text_3.setAutoDraw(False)
    
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

# ------Prepare to start Routine "EyesOpen"-------
t = 0
EyesOpenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(90.000000)
# update component parameters for each repeat
greenProc.setSize(greenSize)
ProcTarget.setSize(pictureSize)
ProcTarget.setImage('./stimuli/images/086.bmp')
ProcPicture.setSize(pictureSize)
ProcPicture.setImage('./stimuli/images/086.bmp')
# Send trial onset marker to LSL
outlet.push_sample('o')
# keep track of which components have finished
EyesOpenComponents = [blackProc, greenProc, ProcTarget, ProcPicture]
for thisComponent in EyesOpenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EyesOpen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EyesOpenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blackProc* updates
    if t >= 0.0 and blackProc.status == NOT_STARTED:
        # keep track of start time/frame for later
        blackProc.tStart = t
        blackProc.frameNStart = frameN  # exact frame index
        blackProc.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blackProc.status == STARTED and t >= frameRemains:
        blackProc.setAutoDraw(False)
    
    # *greenProc* updates
    if t >= 0.0 and greenProc.status == NOT_STARTED:
        # keep track of start time/frame for later
        greenProc.tStart = t
        greenProc.frameNStart = frameN  # exact frame index
        greenProc.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if greenProc.status == STARTED and t >= frameRemains:
        greenProc.setAutoDraw(False)
    
    # *ProcTarget* updates
    if t >= 0.0 and ProcTarget.status == NOT_STARTED:
        # keep track of start time/frame for later
        ProcTarget.tStart = t
        ProcTarget.frameNStart = frameN  # exact frame index
        ProcTarget.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ProcTarget.status == STARTED and t >= frameRemains:
        ProcTarget.setAutoDraw(False)
    
    # *ProcPicture* updates
    if t >= 0.0 and ProcPicture.status == NOT_STARTED:
        # keep track of start time/frame for later
        ProcPicture.tStart = t
        ProcPicture.frameNStart = frameN  # exact frame index
        ProcPicture.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ProcPicture.status == STARTED and t >= frameRemains:
        ProcPicture.setAutoDraw(False)
    
    
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


# ------Prepare to start Routine "waitInterTrial"-------
t = 0
waitInterTrialClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
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
while continueRoutine and routineTimer.getTime() > 0:
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
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blackWaitInterTrial.status == STARTED and t >= frameRemains:
        blackWaitInterTrial.setAutoDraw(False)
    
    # *whiteWaitInterTrial* updates
    if t >= 0.0 and whiteWaitInterTrial.status == NOT_STARTED:
        # keep track of start time/frame for later
        whiteWaitInterTrial.tStart = t
        whiteWaitInterTrial.frameNStart = frameN  # exact frame index
        whiteWaitInterTrial.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
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


# ------Prepare to start Routine "description2"-------
t = 0
description2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyPressRun2 = event.BuilderKeyResponse()
# keep track of which components have finished
description2Components = [polygon2, descriptionText2, keyPressRun2]
for thisComponent in description2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "description2"-------
while continueRoutine:
    # get current time
    t = description2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon2* updates
    if t >= 0.0 and polygon2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon2.tStart = t
        polygon2.frameNStart = frameN  # exact frame index
        polygon2.setAutoDraw(True)
    
    # *descriptionText2* updates
    if t >= 0.0 and descriptionText2.status == NOT_STARTED:
        # keep track of start time/frame for later
        descriptionText2.tStart = t
        descriptionText2.frameNStart = frameN  # exact frame index
        descriptionText2.setAutoDraw(True)
    
    # *keyPressRun2* updates
    if t >= 0.0 and keyPressRun2.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyPressRun2.tStart = t
        keyPressRun2.frameNStart = frameN  # exact frame index
        keyPressRun2.status = STARTED
        # keyboard checking is just starting
        keyPressRun2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if keyPressRun2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            keyPressRun2.keys = theseKeys[-1]  # just the last key pressed
            keyPressRun2.rt = keyPressRun2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in description2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "description2"-------
for thisComponent in description2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyPressRun2.keys in ['', [], None]:  # No response was made
    keyPressRun2.keys=None
thisExp.addData('keyPressRun2.keys',keyPressRun2.keys)
if keyPressRun2.keys != None:  # we had a response
    thisExp.addData('keyPressRun2.rt', keyPressRun2.rt)
thisExp.nextEntry()
# the Routine "description2" was not non-slip safe, so reset the non-slip timer
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
Fixation10Components = [fixation10, fixationImage10, text, text_2, text_3]
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
    
    # *text* updates
    if t >= 7.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 7.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # *text_2* updates
    if t >= 8.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 8.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
    # *text_3* updates
    if t >= 9.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    frameRemains = 9.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_3.status == STARTED and t >= frameRemains:
        text_3.setAutoDraw(False)
    
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

# ------Prepare to start Routine "EyesClose"-------
t = 0
EyesCloseClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(90.000000)
# update component parameters for each repeat
greenProc_2.setSize(greenSize)
ProcTarget_2.setSize(greenSize)
ProcTarget_2.setImage('./stimuli/images/ocean.jpg')
# Send trial onset marker to LSL
outlet.push_sample('c')
# keep track of which components have finished
EyesCloseComponents = [blackProc_2, greenProc_2, ProcTarget_2]
for thisComponent in EyesCloseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EyesClose"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EyesCloseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blackProc_2* updates
    if t >= 0.0 and blackProc_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        blackProc_2.tStart = t
        blackProc_2.frameNStart = frameN  # exact frame index
        blackProc_2.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blackProc_2.status == STARTED and t >= frameRemains:
        blackProc_2.setAutoDraw(False)
    
    # *greenProc_2* updates
    if t >= 0.0 and greenProc_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        greenProc_2.tStart = t
        greenProc_2.frameNStart = frameN  # exact frame index
        greenProc_2.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if greenProc_2.status == STARTED and t >= frameRemains:
        greenProc_2.setAutoDraw(False)
    
    # *ProcTarget_2* updates
    if t >= 0.0 and ProcTarget_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ProcTarget_2.tStart = t
        ProcTarget_2.frameNStart = frameN  # exact frame index
        ProcTarget_2.setAutoDraw(True)
    frameRemains = 0.0 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ProcTarget_2.status == STARTED and t >= frameRemains:
        ProcTarget_2.setAutoDraw(False)
    
    
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


# ------Prepare to start Routine "waitInterTrial"-------
t = 0
waitInterTrialClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
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
while continueRoutine and routineTimer.getTime() > 0:
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
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blackWaitInterTrial.status == STARTED and t >= frameRemains:
        blackWaitInterTrial.setAutoDraw(False)
    
    # *whiteWaitInterTrial* updates
    if t >= 0.0 and whiteWaitInterTrial.status == NOT_STARTED:
        # keep track of start time/frame for later
        whiteWaitInterTrial.tStart = t
        whiteWaitInterTrial.frameNStart = frameN  # exact frame index
        whiteWaitInterTrial.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
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
child.sendline('\r')






# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
