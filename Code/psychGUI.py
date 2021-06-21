import pdb
import os
from subprocess import Popen, PIPE, STDOUT, run, call
from psychopy import gui, core, data
from paths import subject_path_init, osuser_path_init, list_com_ports

"""
This script create a GUI


@author: Soheil Borhani
"""

class mainGUI():
    def __init__(self):

        # find list of available com ports to send event markers
        avail_com_ports = ['']
        avail_com_ports.extend(list_com_ports())

        self.expInfo = {'Participant ID': '', 'Age': '', 'Sex': ['Male', 'Female'],
                        'Handedness': ['Right-handed', 'Left-handed', 'Ambidextrous'],
                        'Data modality': ['Without EEG', 'With EEG'],
                        'EEG headset': ['', 'Emotiv EPOC(+)', 'gtec Unicorn', 'gtec Nautilus 32'],
                        'Visualize Epochs': False,
                        'Audiovisual Cue': [1],
                        'COM Port Marker Receiver': avail_com_ports,
                        'date': [data.getDateStr()]}

    def query(self):
        self.dlg = gui.DlgFromDict(dictionary=self.expInfo, title='GUI', sortKeys=False, screen=-1)
        if not self.dlg.OK:  # or if ok_data is not None
            core.quit()  # user pressed cancel
            quit()
            print('user cancelled')
        return self.expInfo

    def select_mode(self):
        self.expInfo['Experiment Mode'] = ['intro', 'Resting_Eyes_Opened', 'Resting_Eyes_Closed',
                                           'train-A', 'train-B', 'train-A(short)', 'train-B(short)']
        self.dlg = gui.DlgFromDict(dictionary=self.expInfo, title='Continue with choosing the experiment mode...',
                                   sortKeys=False, screen=-1)
        if not self.dlg.OK:  # or if ok_data is not None
            core.quit()  # user pressed cancel
            # kill python
            quit()
            print('user cancelled')
        return self.expInfo
