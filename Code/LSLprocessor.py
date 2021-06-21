# Imports
import numpy as np
from scipy.stats import zscore
import os
import pandas as pd
import mne
from scipy.signal import detrend
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pdb


# EEG PREPROCESSING FUNCTIONS

def scale1DArray(eeg_array, axis=1):
    """
    Scales a 2D array, with scaling on the specified axis.

    # Arguments
        eeg_array: NumPy array
            Array of EEG data in the following format: [channels, time samples].

        axis: int
            Normalization axis.

    # Returns
        X_z: NumPy array
            Scaled data array (mean = 0 and std = 1 along specified axis)
    """
    no_chs = eeg_array.shape[0]
    no_samples = eeg_array.shape[1]

    X_res = np.reshape(eeg_array, (1, no_chs * no_samples))
    X_z = zscore(X_res, axis=axis)

    return X_z


def scale2DArray(eeg_array, axis=1):
    """
    Scales a 3D array to a 2D array, with scaling on the specified axis.

    # Arguments
        eeg_array: NumPy array
            Array of EEG data in the following format: [trials, channels, time samples].

        axis: int
            Normalization axis.

    # Returns
        X_z: NumPy array
            Scaled data array (mean = 0 and std = 1 along specified axis)
    """
    no_trials = eeg_array.shape[0]
    no_chs = eeg_array.shape[1]
    no_samples = eeg_array.shape[2]

    X_res = np.reshape(eeg_array, (no_trials, no_chs * no_samples))
    X_z = zscore(X_res, axis=axis)

    return X_z


def channelInfo(headsetType, sfreq=100):
    """
    Creates an MNE info data structure.

    # Arguments
        reject_ch: boolean
            Whether to reject predefined channels.

        sfreq: int
            Sampling frequency.

    # Returns
        info: MNE info structure
    """
    if headsetType == 'Emotiv EPOC(+)':
        channel_names = ['RAW_CQ', 'AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8',
                         'AF4', 'GYROX', 'GYROY', 'TIMESTAMP']

        channel_types = ['misc'] * 1 + ['eeg'] * 14 + ['misc'] * 3

    elif headsetType == 'gtec Nautilus 32':
        channel_names = ['Fp1', 'Fp2', 'AF3', 'AF4', 'F7', 'F3', 'Fz', 'F4', 'F8', 'FC5', 'FC1', 'FC2', 'FC6', 'T7',
                         'C3', 'C4', 'Cz', 'T8', 'CP5', 'CP1', 'CP2', 'CP6', 'P7', 'P3', 'Pz', 'P4', 'P8', 'PO7', 'PO3',
                         'PO4', 'PO8', 'Oz', 'TIMESTAMP']
        channel_types = ['eeg'] * 32 + ['misc'] * 1

    elif headsetType == 'gtec Unicorn':
        channel_names = ['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8']
        channel_types = ['eeg'] * 8

    montage = 'standard_1020'
    info = mne.create_info(channel_names, sfreq, channel_types, montage)

    return info


def preprocessEpoch(eeg, info, downsample, tmin, reject=None, mne_reject=1, reject_ch=None, flat=None, bad_channels=[],
                    opt_detrend=1, HP=0, LP=40, phase='zero-double'):
    n_samples = eeg.shape[0]
    n_channels = eeg.shape[1]
    eeg = np.reshape(eeg.T, (1, n_channels, n_samples))
    # Baseline start, i.e. 200 ms before stimulus onset

    # Temporal detrending:
    if opt_detrend == 1:
        eeg = detrend(eeg, axis=2, type='linear')

    epoch = mne.EpochsArray(eeg, info, tmin=tmin, baseline=None, verbose=False)

    # Drop list of channels known to be problematic:
    if reject_ch == True:
        # label of channels to remove
        bads = ['RAW_CQ', 'GYROX', 'GYROY', 'TIMESTAMP']
        badSet = set(bads)

        # list of all channel names
        allSet = set(epoch.ch_names)

        # find the intersection of all available channels and bad channels
        badSet = badSet.intersection(allSet)
        badSet = list(badSet)
        epoch.drop_channels(badSet)

    # Lowpass
    epoch.filter(HP, LP, fir_design='firwin', phase=phase, verbose=False)

    # Downsample
    epoch.resample(downsample, npad='auto', verbose=False)

    # Apply baseline correction
    epoch.apply_baseline(baseline=(None, 0), verbose=False)

    if reject is not None:  # Rejection of channels, either manually defined or based on MNE analysis. Currently not
        # used.
        if mne_reject == 1:  # Use MNE method to reject+interpolate bad channels
            from mne.epochs import _is_good
            from mne.io.pick import channel_indices_by_type
            # reject=dict(eeg=100)
            idx_by_type = channel_indices_by_type(epoch.info)
            A, bad_channels = _is_good(epoch.get_data()[0], epoch.ch_names, channel_type_idx=idx_by_type, reject=reject,
                                       flat=flat, full_report=True)
            print(A)
            if A == False:
                epoch.info['bads'] = bad_channels
                epoch.interpolate_bads(reset_bads=True, verbose=False)
        else:  # Predefined bad_channels
            epoch.drop_channels(bad_channels)

    # Re-referencing
    epoch.set_eeg_reference(verbose=False)

    # Apply baseline after re-reference
    epoch.apply_baseline(baseline=(None, 0), verbose=False)

    epoch = epoch.get_data()[0]

    return epoch