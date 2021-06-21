import pdb
import os, sys
import pickle
import time
import numpy as np
from psychopy import gui, core, data
from pylsl import StreamOutlet, StreamInfo, resolve_byprop, local_clock
from pytictoc import TicToc
from subprocess import Popen, PIPE, STDOUT, run, call

from paths import base_dir_init, python_path, viz_path, run_experiment, run_recorder, stop_recorder
import psychGUI

from LSLparser import get_epoch, clear_stream, read_marker_stream, read_EEG_stream, channel_visualize
from LSLprocessor import preprocessEpoch, channelInfo

elapsedTime = TicToc()

"""
Step 0: Open the GUI to navigate into the experiment
"""

# Initiate exp GUI
expGUI = psychGUI.mainGUI()
expInfo = expGUI.query()

stop = False
while not stop:
    ########################################################################################################################
    """
    Step 1: Re-open the GUI to choose the experiment
    """

    # users can decide whether to continue with another session or stop the experiment
    expInfo = expGUI.select_mode()
    ########################################################################################################################
    """
    Step 2: Run experiment and create an empty directory with using the "expInfo['Participant ID']"
    """
    # Run experiment
    save_folder = run_experiment(expInfo)
    time.sleep(2.0)
    print("Experiment script is running for " + expInfo['Experiment Mode'])

    ########################################################################################################################

    """
    Step 3: Look for a recent stream from the Psychopy experimental script (will localize the experimental stream after
     StepOne is started).
    """

    marker_not_present = 1  # Whether to look for a marker stream from other scripts
    timeout = 1  # Time to look for stream in seconds

    while marker_not_present:
        t = local_clock()
        streams = resolve_byprop('type', 'Markers', timeout=timeout)
        for i in range(len(streams)):
            lsl_created = (streams[i].created_at())
            if np.abs(lsl_created - t) < 20:  # Make sure that the stream has been created within the last 20 seconds
                marker_not_present = 0
                print("An LSL Marker stream has been found!")

    ########################################################################################################################
    """
    Step 4: Determine if EEG stream is in the LSL pipe and if experiment marker is sending data into LSL
    """
    inlet_EEG = None
    try:
        if expInfo['Data modality'] in ['With EEG']:
            # Read EEG data stream and experimental script marker stream
            inlet_EEG = read_EEG_stream(max_buf=2)  # EEG stream

        # Experimental marker stream
        inlet_marker = read_marker_stream(stream_name='BluegrassMemoryExperiment')

    except:
        # kill python process associated with unsuccessful running of "exp_process", kill unsuccessful python processes
        Popen('tasklist | find /i "python.exe" && taskkill /im python.exe /F || echo process "python.exe" not running',
              shell=True)
        print("Check experiment script for LSL stream_name!")
        quit()

    ########################################################################################################################
    """
    Step 5: if expInfo['Experiment Mode'] in ['Resting_Eyes_Opened', 'Resting_Eyes_Closed'], data recorder continues 
    as long as the marker from the experimental script is 'e' 
    """

    # Start recording the marker and EEG streams in a separate file for post experiment offline analysis
    # for all expInfo['Experiment Mode'] except 'intro'
    if expInfo['Experiment Mode'] not in ['intro']:
        recorderHandle = run_recorder(expInfo)

    # Handle data recorder for resting-state EEG
    if expInfo['Data modality'] in ['Without EEG'] or \
            (expInfo['Data modality'] in ['With EEG'] and expInfo['EEG headset'] != '' and
            expInfo['Experiment Mode'] in ['intro', 'Resting_Eyes_Opened', 'Resting_Eyes_Closed']):
        while True:
            sample, timestamp = inlet_marker.pull_chunk()
            if len(sample) > 0:
                if 'e' in sample[0]:
                    if expInfo['Data modality'] in ['With EEG'] and expInfo['Experiment Mode'] not in ['intro']:
                        stop_recorder(recorderHandle)
                        clear_stream(inlet_EEG)
                    # # Clear EEG and experiment streams to ensure a clean start
                    clear_stream(inlet_marker)
                    break
    if expInfo['Data modality'] in ['With EEG'] and expInfo['EEG headset'] == '' and \
            expInfo['Experiment Mode'] in ['Resting_Eyes_Opened', 'Resting_Eyes_Closed']:
        print("You have to select an appropriate EEG headset!")
        # kill python
        Popen('tasklist | find /i "python.exe" && taskkill /im python.exe /F', shell=True)
        print("Check experiment script for LSL stream_name!")
        quit()

    ########################################################################################################################
    """
    Step 6: Adjust the LSLparser and LSLprocessor based on the selected hardware
    """
    if expInfo['Data modality'] in ['With EEG']:
        if expInfo['EEG headset'] == '':
            print("You have to select an appropriate EEG headset!")
            # kill python
            Popen('tasklist | find /i "python.exe" && taskkill /im python.exe /F', shell=True)
            print("Check experiment script for LSL stream_name!")
            quit()

        if expInfo['EEG headset'] == 'Emotiv EPOC(+)':
            n_channels = 14
            fs = 128  # Sampling rate

        elif expInfo['EEG headset'] == 'gtec Nautilus 32':
            n_channels = 32
            fs = 250  # Sampling rate

        elif expInfo['EEG headset'] == 'gtec Unicorn':
            n_channels = 8
            fs = 250  # Sampling rate

        # Sampling rate after re-sampling
        fs_new = 100
        # MNE info structures for EEG data
        info_fs = channelInfo(expInfo['EEG headset'], sfreq=fs)
        info_newfs = channelInfo(expInfo['EEG headset'], sfreq=fs_new)

        """
            Step 7: Set up epoch and the experiment parameters
        """

        # Variables for sampling of EEG
        t_latency = 0.0  # Seconds (currently not used)
        baseline_tmin = -0.2  # Seconds (before stimuli onset)
        tmax = 0.80  # Seconds (after stimuli onset)
        n_time = int((tmax - baseline_tmin) * fs_new)

        target_epochs = np.empty((0, n_channels, n_time))
        nontarget_epochs = np.empty((0, n_channels, n_time))

    ########################################################################################################################

    # Parameters' initializations
    excess_EEG = []
    excess_EEG_time = []
    excess_marker = []
    excess_marker_time = []

    target_markers = np.empty(0)
    nontarget_markers = np.empty(0)

    target_RT = np.empty(0)
    nontarget_RT = np.empty(0)

    marker_all = []
    marker_all_Target = []
    marker_all_NonTarget = []
    look_for_trigger = 1

    n_run = 0
    reject = None
    flat = None

    ########################################################################################################################
    """
    Step 8: Parameter definition for behavioral response (keypresses during training)
    """
    num_incorrect = 0
    num_epochs_train = 0
    num_epoch_total = 0

    ########################################################################################################################
    """
    Step 9: If visualization is activated, create an LSL stream to send epochs of EEG 
    during train modes for visualization
    """
    # Check if user wants to visualize epochs of data
    if expInfo['Visualize Epochs']:
        chan_list = channel_visualize(expInfo['EEG headset'])

        # for sending epoched data over LSL, channel_count is the number channels packed in a column and nominal_rate is
        # the number of rows
        info_viz_outlet = StreamInfo(name='viz', type='EPOCH', channel_count=fs_new, nominal_srate=n_channels + 1,
                                     channel_format='float32', source_id='viz')

        # Append channel names to outlet_viz
        chns = info_viz_outlet.desc().append_child('channels')
        for chan in chan_list:
            ch = chns.append_child('channel')
            ch.append_child_value('label', chan)

        # time.sleep(3.0)
        # next make an outlet for epoch visualization
        outlet_viz = StreamOutlet(info_viz_outlet)

        process = Popen("start cmd.exe @cmd /k %s %s %s %s &" % (python_path, viz_path, str(fs_new), str(n_channels)),
                        shell=True, stdout=PIPE)
    ########################################################################################################################
    """
    Step 10: Start sampling (continues as long as the marker from the experimental script is 'e') 
    """
    if expInfo['Data modality'] in ['With EEG'] and expInfo['Experiment Mode'] in ['train-A', 'train-B', 'train-A(short)', 'train-B(short)']:

        while True:
            # Extract epoch
            epoch, behavior_marker, exp_marker, behavior_timestamp, exp_timestamp, excess_EEG, excess_EEG_time, excess_marker, excess_marker_time, \
            look_for_trigger = get_epoch(inlet_EEG, inlet_marker, expInfo['Participant ID'],
                                         excess_EEG, excess_EEG_time, excess_marker, excess_marker_time,
                                         state=expInfo['Experiment Mode'], look_for_trigger=1,
                                         tmin=baseline_tmin, tmax=tmax, fs=fs)
            if len(epoch) > 0:
                num_epoch_total = num_epoch_total + 1

            # Preprocess one epoch at a time and append to stable_blocks array
            if exp_timestamp is not None:
                print(exp_timestamp, exp_marker, behavior_timestamp, behavior_marker, 'RT:',
                      behavior_timestamp - exp_timestamp)

            if behavior_marker in ['1', '2'] and exp_marker in ['a', 'l']:

                # Check if the received behavioral response is within the expected range
                RT = behavior_timestamp - exp_timestamp
                if RT < 1.0:

                    epoch = preprocessEpoch(epoch, info_fs, downsample=fs_new, tmin=baseline_tmin, reject=None,
                                            mne_reject=0,
                                            reject_ch=True, flat=None, bad_channels=[],
                                            opt_detrend=1, HP=0, LP=40, phase='zero-double')

                    if exp_marker == ['a'] and behavior_marker == ['1']:
                        target_epochs = np.append(target_epochs, [epoch], axis=0)
                        target_markers = np.append(target_markers, 1)
                        target_RT = np.append(target_RT, RT)

                        # Check if user wants to visualize epochs of data
                        if expInfo['Visualize Epochs']:
                            label = np.ndarray.tolist(1 * np.ones((1, fs_new)))
                            y = np.ndarray.tolist(epoch) + label
                            outlet_viz.push_chunk(y, pushthrough=True)

                        # meanEpoch = np.mean([lastEpoch, epoch], axis=0)
                        # lastEpoch = epoch
                    elif exp_marker == ['l'] and behavior_marker == ['1']:
                        nontarget_epochs = np.append(nontarget_epochs, [epoch], axis=0)
                        nontarget_markers = np.append(nontarget_markers, 0)
                        nontarget_RT = np.append(nontarget_RT, RT)

                        # Check if user wants to visualize epochs of data
                        if expInfo['Visualize Epochs']:
                            label = np.ndarray.tolist(-1 * np.ones((1, fs_new)))
                            y = np.ndarray.tolist(epoch) + label
                            outlet_viz.push_chunk(y, pushthrough=True)

                    if exp_marker in ['a', 'l'] and behavior_marker in ['2']:
                        num_incorrect = num_incorrect + 1

            elif exp_marker == 'e':
                print('Mean_target_RT: ', round(np.mean(target_RT), 3),
                      ',Mean_target_RT: ', round(np.mean(nontarget_RT), 3),
                      ',Num_Correct_Resp: ', target_epochs.shape[0] + nontarget_epochs.shape[0],
                      ',Num_Incorrect_Resp: ', num_incorrect, ',Total_epochs: ', num_epoch_total)

                if expInfo['Experiment Mode'] not in ['intro']:
                    stop_recorder(recorderHandle)
                    clear_stream(inlet_EEG)
                clear_stream(inlet_marker)
                break

########################################################################################################################
# """
# Step 11: Gracefully terminate the experiment
# """
#
# # Clear out LSL buffer for clean restart and initialization
# clear_stream(inlet_marker)
# clear_stream(inlet_EEG)
# quit()
