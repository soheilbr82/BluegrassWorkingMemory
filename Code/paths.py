# -*- coding: utf-8 -*-
"""
Initialization of paths for system scripts, subjects directory, and experiment.
"""
import pdb
import os
import json
import sys
from sys import platform
from subprocess import Popen, PIPE, STDOUT, run, call
import winpexpect, time
import serial.tools.list_ports as ports
from PyQt5.QtWidgets import QApplication


def base_dir_init():  # Base directory for ClosedLoop GitHub
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return base_dir


def subject_path_init():  # Subjects directory, for storing EEG data
    subject_path = os.path.join(base_dir_init(), 'subjectsData')  # base_dir_init() + '\subjectsData'
    return subject_path


def python_path():  # Subjects directory, for storing EEG data
    python_path = os.path.join(base_dir_init(), 'Python_Engine', 'python.exe')
    return python_path


def viz_path():  # Subjects directory, for storing EEG data
    viz_path = os.path.join(base_dir_init(), 'Code', 'viz_epoch.py')
    return viz_path


def osuser_path_init():  # Subjects directory, for storing EEG data
    subject_path = os.path.join(os.path.join(os.path.expandvars("%userprofile%"), 'BluegrassSTM',
                                             'subjectsData'))  # base_dir_init() + '\subjectsData'
    return subject_path


def subject_logger(save_folder, expInfo):  # Subjects directory, for storing EEG data
    # parse in currect time and date
    currentTime = time.strftime('%m-%d-%y_%H-%M')
    logger = os.path.join(save_folder, currentTime + "_log.txt")
    f = open(logger, "w")
    f.write(str(expInfo))
    f.close()


def list_com_ports():
    com_ports = list(ports.comports())  # create a list of com ['COM1','COM2']
    avail_ports = []
    if com_ports:
        for i in com_ports:
            avail_ports.append(i.device)  # returns 'COMx'
    return avail_ports


# Run Lab Recorder
def run_recorder(expInfo):
    # parse in currect time and date
    currentTime = time.strftime('%m-%d-%y_%H-%M')

    # parse in participant ID
    subjectID = expInfo['Participant ID']

    # parse in experiment mode between "train" and "neurofeedback"
    expMode = expInfo['Experiment Mode']

    # path to LabRecorder
    LabrecorderPath = os.path.join(base_dir_init(), 'lib', 'LabRecorder', 'LabRecorderCLI.exe')

    # path to store lsl streams
    storePath = os.path.join(osuser_path_init(), subjectID)

    # run LabRecorder
    recorder_process = winpexpect.winspawn(
        '%s %s\subject_%s_%s_%s.xdf \'name="Keyboard"\'' % (LabrecorderPath, storePath,
                                                            subjectID, expMode, currentTime))

    return recorder_process


# Stop Lab Recorder
def stop_recorder(recorder_process):
    recorder_process.sendline('\r')


def run_experiment(expInfo):  # Data (images) storage directory

    # path to store lsl streams
    save_folder = os.path.join(osuser_path_init(), expInfo['Participant ID'])
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Save a log file
    subject_logger(save_folder, expInfo)

    # pythonPath = 'python'
    pythonPath = python_path()
    # pythonPath = 'python' # 'C:\ProgramData\Anaconda3\python.exe'
    if expInfo['Experiment Mode'] == 'ForTesting_lastrun':
        exp_path = os.path.join(base_dir_init(), 'Experiments',
                                'ForTesting_lastrun.py')

        # Start experiment
        process = Popen("start cmd.exe @cmd /k %s %s %s &" % (pythonPath, exp_path, expInfo), shell=True,
                        stdout=PIPE)

        process.wait(timeout=20)

    if expInfo['Experiment Mode'] == 'intro':
        exp_path = os.path.join(base_dir_init(), 'Experiments',
                                'STM_Intro_lastrun.py')

        # Start experiment
        process = Popen("start cmd.exe @cmd /k %s %s %s &" % (pythonPath, exp_path, expInfo), shell=True,
                        stdout=PIPE)

        process.wait(timeout=20)

    elif expInfo['Experiment Mode'] == 'Resting_Eyes_Opened':
        exp_path = os.path.join(base_dir_init(), 'Experiments',
                                'Resting_Eyes_Opened_lastrun.py')

        # Start experiment
        process = Popen("start cmd.exe @cmd /k %s %s %s &" % (pythonPath, exp_path, expInfo), shell=True,
                        stdout=PIPE)

        process.wait(timeout=20)

    elif expInfo['Experiment Mode'] == 'Resting_Eyes_Closed':
        exp_path = os.path.join(base_dir_init(), 'Experiments',
                                'Resting_Eyes_Closed_lastrun.py')
        process = Popen("start cmd.exe @cmd /k %s %s %s &" % (pythonPath, exp_path, expInfo), shell=True,
                        stdout=PIPE)

        process.wait(timeout=20)

    elif expInfo['Experiment Mode'] in ['train-A', 'train-B', 'train-A(short)', 'train-B(short)']:
        exp_path = os.path.join(base_dir_init(), 'Experiments',
                                'STM_Train_lastrun.py')
        process = Popen("start cmd.exe @cmd /k %s %s %s &" % (pythonPath, exp_path, expInfo), shell=True,
                        stdout=PIPE)
        process.wait(timeout=20)

    return save_folder


if __name__ == '__main__':
    base_dir = base_dir_init()
    print('====== Current directory ======')
    print(base_dir)
