#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 04, 2021, at 21:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '4'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
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
    originPath='C:\\Projects\\BluegrassSTM_1.8_WithoutAudiovisual_Win64\\Experiments\\Resting_Eyes_Opened_lastrun.py',
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

# Initialize components for Routine "desEyesOpen"
desEyesOpenClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
descriptionText = visual.TextStim(win=win, name='descriptionText',
    text='Eyes open for 1.5 minutes\n\nPlease stare at fixation point\n\n\nTry to be as still as possible\n\nWe will wake you as soon as time is up\n\n\n\n\nPress SPACEBAR to continue',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyPressRun = keyboard.Keyboard()

# Initialize components for Routine "Fixation10"
Fixation10Clock = core.Clock()
fixation = visual.Rect(
    win=win, name='fixation',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
fixationImage = visual.ImageStim(
    win=win,
    name='fixationImage', 
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

# Initialize components for Routine "EyesOpen"
EyesOpenClock = core.Clock()
blackProc = visual.Rect(
    win=win, name='blackProc',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=-1.0, interpolate=True)
greenProc = visual.Rect(
    win=win, name='greenProc',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
ProcTarget = visual.ImageStim(
    win=win,
    name='ProcTarget', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sound_1 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)

# Initialize components for Routine "end"
endClock = core.Clock()
polygon_end = visual.Rect(
    win=win, name='polygon_end',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
end_text = visual.TextStim(win=win, name='end_text',
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





pictureSize=(0.75,1)
greenSize=(1.6,1.2)









# Open LabRecorder
#os.system(".\lib\LabRecorder\LabRecorder.exe")

# Add lsl keypress markers
from pylsl import StreamInfo, StreamInlet, StreamOutlet, resolve_stream
info = StreamInfo(name='BluegrassMemoryExperiment', type='Markers', channel_count=1,
                  channel_format='string', source_id='Keyboard')
# Initialize the keyboard stream.
outlet = StreamOutlet(info)


# Open LabRecorder
#os.system(".\lib\LabRecorder\LabRecorder.exe")


#currentTime = expInfo['date']
#subjectID = expInfo['participant']
#Labrecorder = '.\lib\LabRecorder\LabRecorderCLI.exe'
#Dataset='.\Dataset'

# Open LabRecorder
#import subprocess, sys, os, winpexpect, time
#child =  winpexpect.winspawn('%s %s\%s_%s.xdf \'name="Keyboard"\'' % (Labrecorder,Dataset,subjectID,currentTime))

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

# ------Prepare to start Routine "desEyesOpen"-------
continueRoutine = True
# update component parameters for each repeat
keyPressRun.keys = []
keyPressRun.rt = []
_keyPressRun_allKeys = []
# keep track of which components have finished
desEyesOpenComponents = [polygon, descriptionText, keyPressRun]
for thisComponent in desEyesOpenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
desEyesOpenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "desEyesOpen"-------
while continueRoutine:
    # get current time
    t = desEyesOpenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=desEyesOpenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    
    # *descriptionText* updates
    if descriptionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionText.frameNStart = frameN  # exact frame index
        descriptionText.tStart = t  # local t and not account for scr refresh
        descriptionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionText, 'tStartRefresh')  # time at next scr refresh
        descriptionText.setAutoDraw(True)
    
    # *keyPressRun* updates
    if keyPressRun.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyPressRun.frameNStart = frameN  # exact frame index
        keyPressRun.tStart = t  # local t and not account for scr refresh
        keyPressRun.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyPressRun, 'tStartRefresh')  # time at next scr refresh
        keyPressRun.status = STARTED
        # keyboard checking is just starting
        keyPressRun.clock.reset()  # now t=0
        keyPressRun.clearEvents(eventType='keyboard')
    if keyPressRun.status == STARTED:
        theseKeys = keyPressRun.getKeys(keyList=['space'], waitRelease=False)
        _keyPressRun_allKeys.extend(theseKeys)
        if len(_keyPressRun_allKeys):
            keyPressRun.keys = _keyPressRun_allKeys[-1].name  # just the last key pressed
            keyPressRun.rt = _keyPressRun_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon.tStopRefresh)
thisExp.addData('descriptionText.started', descriptionText.tStartRefresh)
thisExp.addData('descriptionText.stopped', descriptionText.tStopRefresh)
# check responses
if keyPressRun.keys in ['', [], None]:  # No response was made
    keyPressRun.keys = None
thisExp.addData('keyPressRun.keys',keyPressRun.keys)
if keyPressRun.keys != None:  # we had a response
    thisExp.addData('keyPressRun.rt', keyPressRun.rt)
thisExp.addData('keyPressRun.started', keyPressRun.tStart)
thisExp.addData('keyPressRun.stopped', keyPressRun.tStop)
thisExp.nextEntry()
# the Routine "desEyesOpen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation10"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
fixationImage.setSize(pictureSize)
# keep track of which components have finished
Fixation10Components = [fixation, fixationImage, text, text_2, text_3]
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
        if tThisFlipGlobal > fixation.tStartRefresh + 3.0-frameTolerance:
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
        if tThisFlipGlobal > fixationImage.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            fixationImage.tStop = t  # not accounting for scr refresh
            fixationImage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixationImage, 'tStopRefresh')  # time at next scr refresh
            fixationImage.setAutoDraw(False)
    
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
thisExp.addData('fixation.started', fixation.tStartRefresh)
thisExp.addData('fixation.stopped', fixation.tStopRefresh)
thisExp.addData('fixationImage.started', fixationImage.tStartRefresh)
thisExp.addData('fixationImage.stopped', fixationImage.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# ------Prepare to start Routine "EyesOpen"-------
continueRoutine = True
routineTimer.add(92.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('o')

# Send trial onset marker to serial port
if isSerial != '':
    port_serial.write(b'o')
greenProc.setSize(greenSize)
ProcTarget.setSize(greenSize)
ProcTarget.setImage('./stimuli/images/ocean.jpg')
sound_1.setSound('A', secs=2.0, hamming=True)
sound_1.setVolume(1, log=False)
# keep track of which components have finished
EyesOpenComponents = [blackProc, greenProc, ProcTarget, sound_1]
for thisComponent in EyesOpenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EyesOpenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EyesOpen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EyesOpenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EyesOpenClock)
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
        if tThisFlipGlobal > blackProc.tStartRefresh + 90-frameTolerance:
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
        if tThisFlipGlobal > greenProc.tStartRefresh + 90-frameTolerance:
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
        if tThisFlipGlobal > ProcTarget.tStartRefresh + 90-frameTolerance:
            # keep track of stop time/frame for later
            ProcTarget.tStop = t  # not accounting for scr refresh
            ProcTarget.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ProcTarget, 'tStopRefresh')  # time at next scr refresh
            ProcTarget.setAutoDraw(False)
    # start/stop sound_1
    if sound_1.status == NOT_STARTED and t >= 90-frameTolerance:
        # keep track of start time/frame for later
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.tStart = t  # local t and not account for scr refresh
        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
        sound_1.play()  # start the sound (it finishes automatically)
    if sound_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_1.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            sound_1.tStop = t  # not accounting for scr refresh
            sound_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
            sound_1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
thisExp.addData('blackProc.started', blackProc.tStartRefresh)
thisExp.addData('blackProc.stopped', blackProc.tStopRefresh)
thisExp.addData('greenProc.started', greenProc.tStartRefresh)
thisExp.addData('greenProc.stopped', greenProc.tStopRefresh)
thisExp.addData('ProcTarget.started', ProcTarget.tStartRefresh)
thisExp.addData('ProcTarget.stopped', ProcTarget.tStopRefresh)
sound_1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_1.started', sound_1.tStart)
thisExp.addData('sound_1.stopped', sound_1.tStop)

# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# Send trial onset marker to LSL
outlet.push_sample('e')

# Send trial onset marker to serial port
if isSerial != '':
    port_serial.write(b'e')
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
