# -*- coding: utf-8 -*-
"""Functions for finding EEG and marker (trigger points for stimuli onset, from experimental script:
experimentFunctions.py) streams, streaming and saving data, writing transcript files and changing system states for
the neurofeedback system.

@author: Soheil Borhani
"""

# Imports
from pylsl import StreamInlet, StreamInfo, resolve_stream, resolve_byprop
import csv
import keyboard
import time
import numpy as np
import sys
from paths import subject_path_init
import os

subject_path = subject_path_init()
import pdb



def clear_stream(inlet):
    """
    Empties the EEG inlet for samples (pulls all samples from the inlet).
    """
    sample0, timestamp0 = inlet.pull_chunk(max_samples=1500)


def flush_lsl():
    """
    Flush labstreaminglayer streams
    """
    streams = resolve_byprop('type', 'Markers', timeout=1)
    if streams:
        for i in range(len(streams)):
            inlet = StreamInlet(streams[i], max_buflen=1)
            clear_stream(inlet)

    streams = resolve_byprop('type', 'EEG', timeout=1)
    if streams:
        for i in range(len(streams)):
            inlet = StreamInlet(streams[i], max_buflen=1)
            clear_stream(inlet)


def read_EEG_stream(max_buf=2):
    """
    Initializes the EEG stream.
    Timeout is an integer denoting the maximum number of seconds to look for whether an EEG stream is available.

    # Arguments
        fs: int
            Sampling frequency in Hz.

        max_buf: int
            Maximum amount of data to have in the buffer (seconds).

    # Returns
        inlet_EEG: pylsl object
            The EEG recording inlet.

        store_EEG: class object
    """
    try:
        streamsEEG = resolve_byprop('type', 'EEG', timeout=3)
        inlet_EEG = StreamInlet(streamsEEG[0], max_buflen=max_buf)
        print('An EEG stream is found!')
    except:
        print('No EEG stream is detected in LSL!')
        raise Exception
        quit()
    return inlet_EEG


def channel_visualize(args):
    if args == 'Emotiv EPOC(+)':

        return ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']

    elif args == 'gtec Nautilus 32':
        return ['Fp1', 'Fp2', 'AF3', 'AF4', 'F7', 'F3', 'FZ', 'F4', 'F8', 'FC5', 'FC1', 'FC2', 'FC6',
                'T7',
                'C3', 'C4', 'Cz', 'T8', 'CP5', 'CP1', 'CP2', 'CP6', 'P7', 'P3', 'Pz', 'P4', 'P8', 'PO7',
                'PO3', 'PO4', 'PO8', 'Oz']

    elif args == 'gtec Unicorn':
        return ['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8']


def read_marker_stream(stream_name='MyMarkerStream3'):
    """
    Initializes the marker stream (time stamps of the EEG data).

    # Arguments
        stream_name: string

     # Returns
        inlet_marker: pylsl object
            The marker/trigger inlet from experimentFunctions.py script.

        store_marker: class object
    """
    try:
        index_lsl = []
        lsl_created = []
        streams = resolve_byprop('type', 'Markers', timeout=2)  # Look for stream(s)
        for i in range(len(streams)):
            if StreamInfo.name(streams[i]) == stream_name:
                index_lsl.append(i)
                lsl_created.append(streams[i].created_at())  # Store when the stream was created
        if index_lsl:
            if len(index_lsl) > 1:  # Multiple streams available
                index_lsl = index_lsl[np.argmax(lsl_created)]
            else:  # One stream available
                index_lsl = index_lsl[np.argmax(lsl_created)]
            inlet_marker = StreamInlet(streams[index_lsl])
            # store_marker = data_init(500, 'marker')  # Initialize marker object
            # store_marker.header = ['Marker', 'Timestamp']
        else:
            inlet_marker = []
        print('Exp marker stream ' + stream_name + ' is found!')
    except:
        print("No Marker stream with the name " + stream_name + " is detected in LSL!")
        raise Exception
        quit()
    return inlet_marker


def read_save_from_stream(inlet, user_id):
    """
    Reads and saves data from a recording inlet.
    """

    sample, timestamp = inlet.pull_chunk()
    sample = np.asarray(sample)
    timestamp = np.asarray(timestamp)
    # store = save_data(store, sample, timestamp, user_id)
    return sample, timestamp


def get_epoch(inlet_EEG, inlet_marker, user_id, excess_EEG=[], excess_EEG_time=[],
              excess_marker=[], excess_marker_time=[], state='intro', look_for_trigger=1, tmin=-0.2, tmax=1, fs=128):

    t_latency = 0  # latency of EEG in relation to trigger
    t_epoch = tmax - tmin  # length of epoch (seconds)
    s_epoch = int(t_epoch * fs)  # samples in epoch
    look_for_epoch = 1
    use_excess_triggers = 1
    sample_marker = []

    epoch = []  # initialize
    while look_for_epoch:
        # read from marker stream
        # sample_marker = []
        # timestamp_marker = []
        if look_for_trigger:
            sample_marker, timestamp_marker = read_save_from_stream(inlet_marker, user_id)
            # if len(sample_marker) > 0:
            #     print(sample_marker, timestamp_marker)

        # read from EEG stream
        sample_EEG, timestamp_EEG = read_save_from_stream(inlet_EEG, user_id)

        if len(excess_EEG):
            if len(sample_EEG):
                sample_EEG = np.concatenate((excess_EEG, sample_EEG), axis=0)
                timestamp_EEG = np.concatenate((excess_EEG_time, timestamp_EEG), axis=0)
            else:  # if no new EEG data was read
                sample_EEG = excess_EEG
                timestamp_EEG = excess_EEG_time

        # Find stimuli marker onset in EEG

        if len(sample_marker):  # if marker is present
            if sample_marker[-1] in ['a', 'l']:
                exp_marker = sample_marker[-1]
                exp_timestamp = timestamp_marker[-1]
                # Find timesample of EEG nearest stimuli onset plus tmin
                i_start = np.argmin(np.abs(exp_timestamp + t_latency + tmin - timestamp_EEG))
                # find closest sample in the EEG corresponding
                # to marker plus latency and baseline
                t_diff = timestamp_marker + t_latency + tmin - timestamp_EEG[i_start]
                # distance between EEG time sample and marker
                avail_samples = (len(timestamp_EEG) - i_start)  # No. samples from stimuli onset + tmin.
                # i_start is timestamp of the EEG closely matched to timestamp of the marker, minus 0.2 sec
                if avail_samples >= s_epoch:  # if one EEG epoch has been recovered
                    s = avail_samples - s_epoch
                    # samples x channels. Add an epoch of size 900 ms, 450 samples
                    look_for_epoch = 0  # done looking for epoch
                    excess_EEG = sample_EEG[i_start + fs - s:, :]
                    excess_EEG_time = timestamp_EEG[i_start + fs - s:]
                else:
                    look_for_trigger = 1
                    excess_EEG = sample_EEG
                    excess_EEG_time = timestamp_EEG

            if state in ['intro', 'train-A', 'train-B', 'train-A(short)', 'train-B(short)']:
                if sample_marker[-1] in ['1', '2']:
                    behavior_marker = sample_marker[-1]
                    behavior_timestamp = timestamp_marker[-1]
                    # imageOnsetMarker = timestamp_marker
                    # Find timesample of EEG nearest stimuli onset plus tmin
                    i_start = np.argmin(np.abs(exp_timestamp + t_latency + tmin - timestamp_EEG))
                    # find closest sample in the EEG corresponding
                    # to marker plus latency and baseline
                    # t_diff = timestamp_marker + t_latency + tmin - timestamp_EEG[i_start]
                    # distance between EEG time sample and marker
                    avail_samples = (len(timestamp_EEG) - i_start)  # No. samples from stimuli onset + tmin.
                    # i_start is timestamp of the EEG closely matched to timestamp of the marker, minus 0.2 sec
                    if avail_samples >= s_epoch:  # if one EEG epoch has been recovered
                        s = avail_samples - s_epoch
                        epoch = sample_EEG[i_start:i_start + s_epoch, :]
                        # epoch = sample_EEG[i_start:i_start + s_epoch, :]
                        # samples x channels. Add an epoch of size 900 ms, 450 samples
                        look_for_epoch = 0  # done looking for epoch
                        excess_EEG = sample_EEG[i_start + fs - s:, :]
                        excess_EEG_time = timestamp_EEG[i_start + fs - s:]
                    else:

                        look_for_trigger = 0
                        excess_EEG = sample_EEG
                        excess_EEG_time = timestamp_EEG

            if sample_marker in ['e']:
                behavior_marker = []
                behavior_timestamp = np.empty([])
                exp_marker = sample_marker
                exp_timestamp = None
                break

        else:
            # time.sleep(0.1)
            look_for_trigger = 1
            excess_EEG = sample_EEG
            excess_EEG_time = timestamp_EEG

    return epoch, behavior_marker, exp_marker, behavior_timestamp, exp_timestamp, excess_EEG, excess_EEG_time, excess_marker, excess_marker_time, look_for_trigger

