# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 19:50:57 2016

@author: marcus

Settings file for the REDm Professional eye tracker

"""

MY_MONITOR = 'default'              # needs to exist in PsychoPy monitor center

#%% CONNECTION AND TRACKER PARAMS

# Connection information. '127.0.0.1' indicates a one computer setup
port_listen=4444
port_send=5555
ip_send = '127.0.0.1'
ip_listen = '127.0.0.1'

track_mode = 'SMART_BINOCULAR'      # Tracking mode
sampling_freq = 250                  # Sampling rate of eye tracker

geom_profile = 'Default Profile'    # Geometric profile 

average_data = False                # Average gaze data across eyes
filtering = False                   # Use filter to smooth online data

#%% Files and filepaths
delete_temp_idf_files = False       # Delete temporary stored idf files
eye_image_size = (240, 300)         # No eye images with the eye tracker, just
                                    # a placeholder

#%% CALIBRATION PARAMETERS 
autoaccept = 1                      # autoaccept (2), semi autoaccept (1, accept first point) 
                                    # of accept with space bar (0)
                                    
n_cal_points = 5                    # number of calibration points supported: [0, 1, 2, 5, 9, 13] 

cal_speed = 0                       # pacing of calibration / validation targets [slow: 0, fast: 1]
                                    # 0: slow, 1:fast
select_best_calibration = True      # option to run a few calibration and 
                                    # select the best
                                    
reset_calibration_points = False    # Resets calibration points to default 
                                    # locations before calibration starts
                                    
record_data_during_calibration = True # Record data during calibration to idf-file

animate_calibration = False          # Show static points or animated targets
screen = 0                          # Display stimuli on a second screen attached 
                                    # to your computer (1). Single setup (0).

# Parameters to shift and scale the calibration grid
shift_cal_grid_x = 0
shift_cal_grid_y = 0
scale_cal_grid = 1









