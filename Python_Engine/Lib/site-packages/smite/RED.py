# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 19:50:57 2016

@author: marcus

Settings file for the RED250/500 eye tracker
Here we list parameters that can be sent remotely to iView X to override default parameters
OBS! PsychoPy geometric setup should match that entered in iView

"""


MY_MONITOR                  = 'default' # needs to exists in PsychoPy monitor center

#%% CONNECTION AND TRACKER PARAMS

# This should mirror settings in iView. You also need to set the IP addresses on both computers (if two computer setup)
port_listen=4444
port_send=5555
ip_send = '192.168.0.2'
ip_listen = '192.168.0.1'

sampling_freq = 500 # Sampling rate of eye tracker

# OBS! The following commands do not seem to work. Change manually in iview instead (setup -> tracking).
average_data = False
filtering = False # Use filters 

#%% Files and filepaths
temp_folder_path = r"C:\\ProgramData\SMI\iViewX\temp"
delete_temp_idf_files = False

eye_image_size = (80, 344)# Size of eye images in RED

#%% CALIBRATION PARAMETERS 
autoaccept = 0  # autoaccept (2), semi autoaccept (1, accept first point) of accept with space bar (0)
n_cal_points = 2  # number of calibration points [2, 5, 9] supported
cal_speed = 1   # pacing of calibration / validation targets 0: slow, 1:fast
select_best_calibration = True # option to run a few calibration and select the best
reset_calibration_points = False # Resets calibration points to default locations
record_data_during_calibration = True
animate_calibration = True # Show static points or animated targets
screen = 0

# Parameters to shift and scale the calibration grid
shift_cal_grid_x = 0
shift_cal_grid_y = 0
scale_cal_grid = 1










