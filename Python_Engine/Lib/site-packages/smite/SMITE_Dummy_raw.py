#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Load required packages 
from psychopy import core, event, misc
from iViewXAPI import*
from iViewXAPIReturnCodes import* 
import subprocess
import numpy as np
import os
from threading import Thread
import helpers
import time


# Numbers used by iView X for identify eye trackers
ET_server_dict = {'iViewX':0, 'iViewXOEM':1, 'iViewNG':2}
ET_device_dict = {'NONE':0, 'RED':1, 'REDm':2, 'RED250Mobile':2, 'HiSpeed':3,
                  'MRI':4, 'HED':5, 'Custom':7, 'REDn':8}	

tracking_mode_dict = {'SMART_BINOCULAR':0, 'MONOCULAR_LEFT':1,
                      'MONOCULAR_RIGHT':2, 'BINOCULAR':3, 
                      'SMART_MONOCULAR':4}
      
#%% To construct a nested Class for sample
# self.sample.leftEye.gazeX = x
#        self.sample.leftEye.gazeY  = y
#        self.sample.rightEye.gazeX = x
#        self.sample.rightEye.gazeY = y
class Dir:
    def __init__(self):
        self.gazeX = 0
        self.gazeY = 0
        
class Eye:
    def __init__(self):
        self.leftEye = Dir()
        self.rightEye = Dir()
#%%    
        
class Connect(Thread):
    """
    Basic functionally to communicate with and manage SMI eye trackers
    """
    def __init__(self):
        '''
        Constructs an instance of the SMITE interface, with specified settings. 
        If settings is not provided, the name of an eyeTracker should 
        be given, e.g., RED-m
        '''
        
        # Create gaze sample
        self.sample = Eye()
            
        self.clock = core.Clock()
        self.connect_timeout = 30 # in seconds 
        self.mouse = event.Mouse()
        self.buf = []
        

        
    #%%
    def init(self):
        
        print('Dummy connected')
     
    #%% 
    def abort_calibration(self):        
        ''' Aborts calibration
        All system supported
        '''
        print('abort_calibration')
    
        
    #%% 
    def abort_calibration_point(self):        
        ''' Aborts calibration point
        Supported systems: REDn, RED250 Mobile
        '''
        print('abort_calibration_points')  

            #%%             
    def accept_calibration_point(self):
        ''' Wait for accept 
        All system supported
        '''        
        print('accept_calibration_points')
        
        
    #%%                     
    def change_calibration_point(self, number, positionX, positionY):
        ''' Change calibration point 'number' to a new position (positionX, positionY)
        All system supported (WARNING: should not be done on the remotes unless
        you REALLY know what you're doing. So don't do it.)       
        '''
        print('change_calibration_point')
            
        
    #%%
    def clear_aoi(self):
        ''' Removes all trigger AOIs
        Not supported. Use your own code and data from the buffer instead
        Supported systems: RED, RED-m, HiSpeed 
        ''' 
        
        print('clear_aoi')  
        
    #%%             
    def clear_recording_buffer(self):
        ''' Clears recording buffer from all recorded data
        Supported systems: all
        '''         
        print('clear_recording_buffer')
        
        
    #%%             
    def configure_filter(self, filter_type=0, filter_action=1):
        '''
        Queries or sets filter parameters. The usage of the parameter data depends on the parameter action
        Args: filter_type: 0 - averaging disabled, 1 - averaging enabled
              filter_action: 0 - query the current filter status (output passed to variable 'filter_status'), 
                              1 - configure filter parameters
        Supported systems: all but REDn
        
        WARNING: For some reason, the only combination that works is filter_type=0, filter_action=1, 
        which means that avaraging is disabled. On the other hand, this is not problem. If you want averaged data, just
        average data from the left and the right eye yourself.
        Let me know if you know how to fix it.

        Returns: 
              filter_status - outputs the current filter status (does not work)
        '''
        
        print('configure_filter')
        
        return None

        
    #%%     
    def connect(self, ip_listen, port_listen, ip_send, port_send, 
                connect_timeout=30):
        ''' Connect to eye tracker server
        Supported systems: all 
        '''
        print('connect')
        
    #%% 
    def continue_eye_tracking(self):
        '''
        Wakes up and enables the eye tracking application from suspend mode to continue processing gaze
        data. The application can be set to suspend mode by calling iV_PauseEyetracking        
        
        Supported systems: all but RED and HiSpeed

        '''
        print('continue_eye_tracking')  
        
    #%% 
    def continue_recording(self, msg):
        '''
        Continues gaze data recording. iV_ContinueRecording does not return until gaze recording is continued.
        Before it can be continued, the data needs to be paused using. iV_PauseRecording. Additionally this
        function allows a message to be stored inside the idf data buffer.        
        
        Supported systems: all
        '''       
        
        print('continue_recording')     
        
    #%% 
    def define_aoi(self, aoi_data):
        '''
        Defines an AOI. The API can handle up to 20 AOIs
        
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            aoi_data - struct, see SDK manual for description
        '''     
        
        print('define_aoi')             

    #%% 
    def define_aoi_port(self, port):
        '''
        Selects a port for sending out TTL trigger
        
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            port - int
        '''  
        
        print('define_aoi_port')           
        
    #%% 
    def delete_red_geometry(self, profile):
        '''
        Deletes the geometry setup with the given profile name. It is not possible 
        to delete a geometry profile if it is currently in use. 
        See chapter Setting up RED Geometry in the iView X SDK Manual.
        
        Supported systems: all but HiSpeed
        '''              
        print('delete_red_geometry') 
        
    #%% 
    def disable_aoi(self, aoi_name):
        '''
        Disables all AOIs with the given name.
        
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            port - int
        '''  
        
        print('disable_aoi')            
        
    #%% 
    def disable_aoi_group(aoi_group):
        '''
        Disables an AOI group
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            port - int
        '''  
        
        print('disable_aoi_group')         
        
    #%% 
    def disable_gaze_data_filter(self):
        '''
        Disables the raw data filter. The gaze data filter can be enabled using 
        iV_EnableGazeDataFilter.        
        Supported systems: all 

        '''   
        print('disable_gaze_data_filter') 
        
      
        
    #%% 
    def disable_processor_high_performance_mode(self):
        '''
        Disables a CPU high performance mode allowing the CPU to reduce the performance.
        Supported systems: all but RED and Hi-Speed
        '''
        print('disable_processor_high_performance_mode')            
  
    #%% 
    def disconnect(self):
        ''' Disconnects the eye tracker 
        Supported systems: all
        '''
        print('disconnect')            

        
    #%% 
    def enable_aoi(self, aoi_name):
        '''
        Enables all AOIs with the given name
        Supported systems: all but RED-n and RED250 mobile.
        '''  
        
        print('enable_aoi')            
           
        
    #%% 
    def enable_aoi_group(self, aoi_group):
        '''
        Disables an AOI group
        Supported systems: all but RED-n and RED250 mobile.
        '''
        
        print('enable_aoi_group')  
        
    #%%                         
    def enable_gaze_data_filter(self):
        '''
        This API bilateral filter was implemented due to special human-computer
        interaction (HCI) application requirements. It smoothes gaze position data in EyeDataStruct::gazeX and
        EyeDataStruct::gazeY contained in SampleStruct, e.g. obtained by iV_GetSample. The gaze data filter
        can be disabled using iV_DisableGazeDataFilter   
        '''
        print('enable_aoi_group')  
        
        
    #%% 
    def enable_processor_high_performance_mode(self):
        '''
        Enables a CPU high performance mode allowing the CPU to reduce the performance.
        Supported systems: all but RED and Hi-Speed
        '''
        print('enable_processor_high_performance_mode')      
        
    #%%
    def get_accuracy(self, visualization = 0):
        ''' Get accuracy. Only possible after a successful validation
        If the parameter visualization is set to 1 the accuracy
        data will be visualized in a dialog window.
        ''' 
        print('get_accuracy')      
        return (None, None, None, None)

    #%%         
    def get_accuracy_image(self, fname=None):
        ''' Returns validation screen image and optinally save it to disk
        '''
        print('get_accuracy_image')      
        
    #%% 
    def get_aoi_output_value(self):
        '''
        Returns the current AOI value.
        Supported systems: all 
        '''  
        print('get_aoi_output_value')    
        
        return None
        
    #%%
    def get_calibration_parameter(self):
        ''' Updates stored calibrationData information with currently selected 
            parameters.
        Supported systems: RED-n and RED250 Mobile 
        '''
        
        print('get_calibration_parameter')    
        
        return None
        
    #%%
    def get_calibration_point(self, calibration_point_number):
        ''' Delivers information about a calibration point.
        Supported systems: all
        '''
        
        
        print('get_calibration_point')    
        
        return None
        
    #%%
    def get_calibration_quality(self, calibration_point_number):
        ''' Delivers fixation quality information about a calibration point. 
        If the passed parameter left or right is NULL, no data will be returned
        Supported systems: RED-n and RED250 Mobile 
        '''      
        
        print('get_calibration_quality')    
        
        return None, None
        
    #%%
    def get_calibration_quality_image(self):
        ''' 
        Same functionally as get_accuracy_image
        Supported systems: RED-n and RED250 Mobile         
        '''   
        
        print('get_calibration_quality_image')    
        
        return None
        
    #%%
    def get_calibration_status(self):
        ''' Updates calibrationStatus information. 
        The client needs to be connected to the iView eye tracking server.
        Supported systems: all        
        ''' 
        
        print('get_calibration_status')    
        
        return None       

    #%%
    def get_current_calibration_point(self):
        ''' Updates data in currentCalibrationPoint with the current calibration 
        point position
        Supported systems: all        
        '''
        print('get_current_calibration_point')    
        
        return None, None      

    #%% 
    def get_current_RED_geometry(self):
        '''
        Supported systems: all but HiSpeed
        '''        
        print('get_current_RED_geometry')    
        
        return None       
    
    #%% 
    def get_current_time_stamp(self):
        ''' Provides the current eye tracker timestamp in microseconds
        Supported systems: all
        '''        
        print('get_current_time_stamp')    
        
        return None       
    
    #%%
    def get_device_name(self):
        ''' Queries the device name information of the connected device.
        Supported systems: all but RED and HiSpeed
        '''                
        print('get_device_name')    
        
        return None       
    
    #%%
    def get_event(self):
        ''' Updates data from eventDataSample with current event data.
        Supported systems: all but RED-n professional
        '''                
        print('get_event')    
        
        return None             
    
    #%%                     
    def get_eye_image(self):
        ''' Updates imageData with current eye image (format: monochrome 8bpp).
        Supported systems: ToDo
        '''   
        print('#%%')    
        
        return None, None     

    #%%
    def get_feature_key(self):
        ''' Gets the device specific feature key. Used for RED-OEM, RED250mobile and REDn devices only
        Supported systems: RED-n and RED250 Mobile
        '''                
        
        print('get_feature_key')    
        
        return None 

    #%%
    def get_gaze_channel_quality(self):
        ''' Retrieve gaze quality data. Fills qualityData with validated accuracy results. Before quality data is
        accessible the system needs to be validated with iV_Validate
        Supported systems: RED-n and RED250 Mobile
        
        ''' 
        
        print('get_gaze_channel_quality')    
        
        return None 
        
    #%%
    def get_recording_state(self):
        ''' Queries the recording state of the eye tracking server. 
        This function can be used to check if the eye
        tracking server is currently performing a recording.
        Supported systems: RED-n and RED250 Mobile
        '''             
        
        print('get_recording_state')    
        
        return None 

    #%% 
    def get_RED_geometry(self):
        ''' Gets the geometry data of a requested profile without selecting them.
        Supported systems: all but HiSpeed
        '''                
        print('get_RED_geometry')    
        
        return None  


    #%%             
    def get_sample(self):
        ''' Updates data in sampleData with current eye tracking data.
        Supported systems: all
        ''' 
        print('get_sample')    
        
        return None 
    
    #%%
    def get_scene_video(self):
        ''' Updates imageData with current scene video image (format: RGB 24bpp)
        Not Supported 
        '''     
        
    #%%
    def get_serial_number(self):
        ''' Retrieve the serial number information of the connected device.
        Supported systems: all but RED and HiSpeed
        '''       
        
        print('get_serial_number')    
        
        return None 
    #%%
    def get_speed_mode(self):
        ''' This function retrieves the speed modes used and supported by the 
        connected iView eye tracking server
        
        speedModes:
        int numberOfSpeedModes - number of supported speed modes
        int speedMode - the current sampling frequency
        int speedModes - an array of sampling frequencies supported by the connected iView eye tracking server;
        int version - version of the current data structure        
        Supported systems: RED-n and RED250 Mobile
        '''       
        
        print('get_speed_mode')    
        
        return None       
    
    #%%             
    def get_system_info(self):
        '''
        int API_Buildnumber build number of iView X SDK in use
        int API_MajorVersion - major version number of iView X SDK in use
        int API_MinorVersion - minor version number of iView X SDK in use
        int iV_Buildnumber - build number of iView eye tracking server in use
        enum ETDevice- 	iV_ETDevice type of eye tracking device
        int iV_MajorVersion - major version number of iView eye tracking server in use		
        int iV_MinorVersion - major version number of iView eye tracking server in use		
        int samplerate
        
        ETDevice {
        NONE = 0, RED = 1, REDm = 2, HiSpeed = 3,
        MRI = 4, HED = 5, Custom = 7, REDn = 8 }	
        
        Supported systems: all        
        '''
    
        print('get_system_info')    
        
        return None     
    
    #%%     
    def get_tracking_mode(self):
        ''' Get eye tracking mode (see set_tracking_mode)
        ''' 
    
        print('get_tracking_mode')    
        
        return None      
    
    #%%         
    def get_tracking_monitor(self):
        ''' Returns validation screen image and optinally save it to disk
        
        The tracking monitor image depicts the positions of both eyes and shows notification arrows 
        if the participant is not properly positioned infront of the eye tracker. 
        The tracking monitor is useful to validate the positioning before and 
        during a recording session.  
        
        Supported systems: all but HiSpeed                   
        '''
        
        print('get_tracking_mode')    
        
        return None, None  
    
    #%% 
    def get_tracking_status(self):
        ''' Updates trackingStatus with current tracking status.
        This function can be used to get the current eye positions.
        
        Supported systems: all 
        
        '''
        print('get_tracking_status')    
        
        return None     
    
    #%%
    def get_use_calibration_key(self):
        ''' Gets the currently set interaction key status for the calibration and validation process. 
        If enableKeys is 0 all available user interaction keys:
            • SPACE for accepting calibration/validation points
            • ESC for aborting calibration/validation
            • TAB for skipping a point (only SMI iViewRED 4.2 or later)
        are disabled.
        
        Supported systems: RED-n and RED250 Mobile 
        '''
        
        print('get_use_calibration_key')    
        
        return None      
    
    
    #%%
    def hide_accuracy_monitor(self):
        ''' Hides accuracy monitor window which can be opened by iV_ShowAccuracyMonitor.
        Supported systems: all
        '''     
        print('hide_accuracy_monitor')    
        
    #%%
    def hide_eye_image_monitor(self):
        ''' Hides eye image monitor window which can be opened by iV_ShowEyeImageMonitor.
        Supported systems: all but RED-n professional
        '''     
        
        print('hide_eye_image_monitor')    
      

    #%%
    def hide_scene_video_monitor(self):
        ''' Hides scene video monitor window which can be opened by iV_ShowSceneVideoMonitor.
        Not Supported 
        '''   

                #%%
    def hide_tracking_monitor(self):
        ''' Hides tracking monitor window which can be opened by iV_ShowTrackingMonitor
        Supported systems: all but HiSpeed
        '''  
        print('hide_tracking_monitor')         
        
    #%% 
    def is_connected(self):
        ''' Checks if connection to iView eye tracking server is still established.
        Supported systems: all 
        
        Returns:
            res - 1 if intended functionality has been fulfilled
                  0 if no connection established
        
        '''
        
        print('is_connected')    
        
        return None   
    
    #%%         
    def load_calibration(self, name):
        ''' Loads a previously saved calibration. A calibration has to be saved by using iV_SaveCalibration.
        
        Supported systems: all 
        
        '''        
        print('load_calibration')    
            
    #%%         
    def log(self, msg):
        ''' Writes logMessage into log file
        
        Supported systems: all 
        
        '''        
        print('log')         
        
    #%%
    def pause_eye_tracking(self):
        ''' Suspend the eye tracking application and disables calculation of gaze data. 
        The application can be reactivated by calling iV_ContinueEyetracking.
        Supported systems: all but RED and HiSpeed
        '''     
        
        print('pause_eye_tracking')             
        
    #%%
    def pause_recording(self):
        ''' Pauses gaze data recording. iV_PauseRecording does not return until 
        gaze recording is paused.
        Supported systems: all 
        '''    
        
        print('pause_recording')        
        
    #%% 
    def quit_server(self):
        ''' Disconnects and closes iView eye tracking server. 
        After this function has been called no other function
        or application can communicate with iView eye tracking server.
        '''
        
        print('quit_server')    
        
    #%% 
    def recalibrate_one_point(self, calibration_point_number):
        ''' Restarts a calibration procedure with a point from the latest calibration process. 
        The point is specified
        by its index in the calibration point profile (counted from 1). If the 
        requested point is not found, an error
        code will be returned. The number of calibration points can be retrieved 
        via iV_GetCalibrationQuality
        
        Supported systems: RED-n and RED250 Mobile 
        '''
        
        print('recalibrate_one_point')         
        
        
    #%%
    def release_aoi_port(self):
        ''' Releases the port for sending TTL trigger.
        Supported systems: all but RED-n and RED250 Mobile 
        '''
        
        print('release_aoi_port')  
        
    #%%
    def remove_aoi(self, name):
        ''' Removes all AOIs with the given name.
        Supported systems: all but RED-n and RED250 Mobile 
        '''   

        print('remove_aoi')  
        
    #%%                         
    def reset_calibration_points(self):           
        ''' Resets the positions of the calibration points
        Supported systems: all 
        
        '''         
        print('reset_calibration_points')       
        
    #%%    	
    def save_calibration(self, name):
        ''' Saves a calibration with a custom name. To save a calibration it 
        is required that a successful calibration already has been completed.
        
        Supported systems: all 
        
        '''
        print('save_calibration')        
        
    #%%             
    def save_data(self, filename, description = "", 
                   user = None, overwrite=0):
        ''' Writes recorded data buffer to disc. 
        The data recording needs to be stopped using iV_StopRecording
        before the data buffer can be saved to given location. 
        The filename can include the path. If the connected eye tracking device 
        is an HED, scene video buffer is written, too. iV_SaveData will not return
        until the data has been saved.
        
        If there is already a file with a certain name 'name.idf', this file will not 
        be overwritten, but save as another file with name 'name_1.idf'.
        
        Args:
            filename - full path including the filename of the data file being created
            description - Optional experiment description tag stored in the idf file. This tag is available in BeGaze and in the text export from an idf file.
            user - Optional name of test person. This tag is available in BeGaze and in the text export
                    from an idf file.
            overwrite - Overwriting policy.
            • 0: do not overwrite file filename if it already exists
            • 1: overwrite file filename if it already exists
        
        Supported systems: all 
        
        '''
                    
        # Set the use equal to the filename if not explicitly given
        if user == None:
            user = filename
            
        # Split filename into path and filename
        path, filename = os.path.split(filename)
        assert(len(path) > 0), "Filename must have a path"
        assert(len(filename) > 0), "Filename must be given"

        # Check if a '.idf was added to the filename. If so, remove it
        ext = os.path.splitext(filename)[1]
        if '.idf' in ext:
            filename = filename.strip('.idf')
            
        print('save_data')          
        
    #%% 
    def select_RED_geometry(self, profile):
        ''' Selects a predefined geometry profile. 
        
        Supported systems: all but HiSpeed 
        
        '''
        print('select_RED_geometry') 
        
    #%%
    def send_command(self, cmd):
        ''' Sends a remote command to iView eye tracking server. 
        Please refer to the iView X help file for further information about remote commands.
        
        Supported systems: all 
        '''
        print('send_command')    
        
    #%%             
    def send_image_message(self, msg):
        ''' Sends a text message to iView X idf recording data file. 
        If the etMessage has the suffix ".jpg", ".bmp",
        ".png", or ".avi" BeGaze will separate the data buffer 
        automatically into according trials.
        
        Supported systems: all 
        '''
        print('send_image_message')     
        
    #%%
    def set_aoi_hit_callback(self, callback_function):
        ''' Sets a callback function for the AOI hit functions.
        Supported systems: all but RED-n and RED250 Mobile
        
        '''
        print('set_aoi_hit_callback')        
        
    #%%
    def set_calibration_callback(self, callback_function):
        ''' Sets a callback function for the AOI hit functions.
        Supported systems: All
        '''           
        
        print('set_calibration_callback')               
        
    #%%
    def set_connection_timeout(self, time):
        ''' Defines a customized timeout for how long iV_Connect tries to 
        connect to iView eye tracking server.
        Supported systems: all but RED-n professional 
        '''          
        
        print('set_connection_timeout')    

    #%%
    def set_event_callback(self, callback_function):
        ''' Sets a callback function for the event data. 
        The function will be called if a real-time detected fixation has
        been started or ended.
        Supported systems: all but RED-n professional 
        '''          
        
        print('set_event_callback')    
        
    #%%
    def set_event_detection_parameters(self, name):
        ''' Defines the detection parameter for online fixation detection algorithm.
        Supported systems: all but RED-n professional 
        '''          
        
    #%%
    def set_eye_image_callback(self, callback_function):
        ''' Sets a callback function for the eye image data. 
        Supported systems: all but RED-n professional and RED-mx
        '''     
        
        print('set_eye_image_callback')  
        
    #%%
    def set_licence(self, key):
        ''' Sets the customer license (required only for OEM devices!).
        Supported systems: RED-n and RED-n scientific
        '''             
        
        print('set_licence')     
        
    #%%
    def set_logger(self, log_level=1, filename='iv_logfile'):
        ''' Sets the customer license (required only for OEM devices!).
        
        ToDo: What log levels are there and what do they mean?
        Supported systems: all 
        
        '''             
        
        print('set_logger')  
    #%%
    def set_resolution(self, stimulus_width, stimulus_height):
        ''' Sets the customer license (required only for OEM devices!).
        
        Defines a fixed resolution independent to the screen resolution of 
        chosen display device defined in iV_-SetupCalibration function.
        
        Could be useful when using real-time data with a screen with low resolution.
        Supported systems: all 
        
        '''             
        
        print('set_resolution')  
        
    #%%
    def set_RED_geometry(self, function_name):
        ''' Define the eye trackers stand alone and monitor integrated geometry
        
        Supported systems: all but HiSpeed
        
        '''             
        print('set_RED_geometry')        
    #%%
    def set_sample_callback(self, function_name):
        ''' Sets a callback function for the raw sample data. 
        The function will be called if iView eye tracking server
        has calculated a new data sample.
        Attention: Algorithms with high processor usage and long calculation 
        time should not run within this callback due to a higher probability of data loss
        Supported systems: all 
       
        '''             
        
        print('set_sample_callback')   
        
    #%%
    def set_scene_video_callback(self, name):
        ''' Sets a callback function for the scene video image data. 
        The function will be called if a new scene video
        image is available. The image format is RGB 24bpp.
        Not Supported. 
        '''    

    #%%
    def set_speed_mode(self, samplingrate):
        ''' This function requests the iView eye tracking server to switch the
        eye tracking frequency to the specified value. Use iV_GetSpeedModes 
        to get the available speed modes for the connected eye tracking device.
        Supported systems: RED-n 
        '''        
        
        if self.set_sampling_freq_allowed:
            print('set_speed_mode')   
        else:
            print("WARNING: set_speed_mode is not supported on this eye tracker")
            
    #%%     
    def set_tracking_mode(self, mode):
        ''' This function is available with SMI iViewRED 4.4 or later and replaces the iV_SetTrackingParameter
            function
            
            e.g., set_tracking_mode(self, 'SMART_BINOCULAR')
        
            Eye tracking modes:
        
            smart_binocular: tracks both eye separately, but can handle temporal monocular loss (default)
            smart_binocular_right/left: both eye visible, but one one dominant (e.g., obvious squinting)
            monocular_right/left: only one eye visible
            
            0 - SmartBinocular SmartBinocular mode.
            1 - MonocularLeft Monocular mode using only the left eye.
            2 - MonocularRight Monocular mode using only the right eye.
            3 - Binocular Binocular mode.
            4 - SmartMonocular SmartMonocular mode.	
            
        Supported systems: all but RED and HiSpeed 
            '''
        if self.set_tracking_mode_allowed:
            assert (mode == 'SMART_BINOCULAR' or 
                    mode == 'MONOCULAR_LEFT' or 
                    mode == 'MONOCULAR_RIGHT' or 
                    mode == 'BINOCULAR' or 
                    mode == 'SMART_MONOCULAR')
            
            print('set_tracking_mode')  
        else:
            print("WARNING: set_tracking_mode is not supported on this eye tracker")          
            
    #%%
    def set_tracking_monitor_callback(self, function_name):
        ''' Sets a callback function for the tracking monitor image data. 
        The function will be called if a new tracking
        monitor image was calculated. The image format is BGR 24bpp
        Supported systems:  all but HiSpeed
        '''    

        print('set_tracking_monitor_callback')  
        
        
    #%%     
    def set_tracking_parameter(self, eye_type=0, parameter_type=4, activate=1):       
        ''' Sets iView eye tracking server tracking parameters. 
        See Eye Tracking Parameter subsection and iView eye tracking server 
        manual for further explanations. Important note: This function can 
        strongly affect tracking stability of your iView X and 
        eyetracking-server system. Only experienced users should use this
        function.
        
        Args:
            eye_type - select specific eye (0 is left, 1 is right)
            parameter_type - parameter to set (see manual)
            activate - new value for selected parameter
            
        Supported systems: ToDo 
        '''          
        print('set_tracking_parameter') 
        
    #%%     
    def setup_calibration_parameters(self,
                                     autoaccept=1,
                                     bg_color=0,
                                     screen=1,
                                     fg_color=0,
                                     cal_method=5, 
                                     cal_speed=1,
                                     target_size=20, 
                                     target_shape=2): 
                                                            
        """
        Sets the calibration and validation visualization parameter.
        
        Setup calibration parameters (but do not initiate calibration)
        An option to define position of calibration point
        
        1 - autoAccept
        2-  background Brightness
        3-  displayDevice
        4 - foreground Brightness
        5 - cal method
        6 - speed (cal)
        7 - target Filename[256]
        8 - targetShape
        9 - targetSize
        10 - visualization
        
        Supported systems: all 
        
        
        """
        
        print('setup_calibration_parameters')     
        
    #%%
    def setup_debug_mode(self, enable_debug_mode=False):
        '''Enables or disables the debug mode for the current connection. 
        The debug mode disables the automatic
        connection termination after 5 seconds of an unresponsive server or client. 
        This can happen e.g. during
        debugging a client application. Beware: the debug mode must not be enabled 
        for production code, as it
        makes the connection status detection of all API functions unreliable!
                
        Supported systems: ?
        '''
        print('setup_debug_mode')                
        
    #%%
    def setup_ltp_recording(self, port_name, enable_recording):
        '''Enables or disables the LPT signal recording functionality. 
        Not Supported. 
        '''     
        
        print('setup_ltp_recording')                
            
    #%%
    def set_use_calibration_key(self, mode):
        ''' Sets and resets the interaction keys during the calibration and validation process.
        See get_use_calibration_key
        '''
        print('set_use_calibration_key')         
        
    #%%
    def show_accuracy_monitor(self):
        '''The validated accuracy results will be visualized in a separate window. 
        Before the image can be drawn the calibration needs to be performed with 
        iV_Calibrate and validated with iV_Validate.
        Supported systems: all
        '''      
        print('show_accuracy_monitor')  
        
    #%%
    def show_eye_image_monitor(self):
        '''Visualizes eye image in a separate window while the participant is 
        beeing tracked (equal to image obtained with iV_GetEyeImage).
        Supported systems: all but RED-n professional and RED-m mx
        '''     
        
        print('show_eye_image_monitor')        
        
    #%%
    def show_scene_video_monitor(self):
        '''Visualizes scene video in separate window.
        Only available for HED devices.
        Not Supported. 
        '''           
        
    #%%
    def show_tracking_monitor(self):
        '''Visualizes RED tracking monitor in a separate window.
        Supported systems: all but HiSpeed
        '''     
        
        print('show_tracking_monitor')      

    #%% 
    def start_iview_server(self, et_application):
        '''Starts the iView eye tracking server application. Depending on the PC, 
        it may take several seconds to start the iView eye tracking server application. 
        The connection needs to be established separately using iV_Connect. 
        The connection timeout can be extended using iV_SetConnectionTimeout.
        
        Supported systems: all 
        '''               
        print('start_iview_server') 
        
    #%%             
    def start_recording(self):
        ''' Starts gaze data recording
        Supported systems: all
        '''
        print('start_recording')      
        
    #%%             
    def stop_recording(self):
        ''' Stops gaze data recording
        Supported systems: all
        '''
        print('stop_recording')      
        
    #%%
    def test_ttl(self, value):
        '''Sends a TTL value to defined port. Define a port with iV_DefineAOIPort
        Supported systems: all
        '''
        print('test_ttl')      

    #%%    
    def validate_iview(self):
        ''' Starts a validation procedure. To proceed, the participant needs to 
        be tracked and has to fixate the validation point. 
        Depending on the validation settings (which can be changed using iV_SetupCalibration
        and iV_SetUseCalibrationKeys) the user can accept the validation points 
        manually (by pressing [SPACE] or calling iV_AcceptCalibrationPoint) or 
        abort the validation (by pressing [ESC] or calling iV_AbortCalibration)
        If the validation is visualized by the 
        API (CalibrationStruct::visualization is set to 1) the function will not
        return until the validation has been finished (closed automatically) 
        or aborted (by using [ESC]).
        If the CalibrationStruct::visualization is set to 0, the function call returns immediately. 
        The user has to implement the visualization of validation points. 
        Information about the current validation point can be retrieved with 
        iV_GetCurrentCalibrationPoint or with setting up the calibration callback using
        iV_SetCalibrationCallback.
        ''' 
        print('validate_iview')    
        
    ###############################################################################
    '''
    Below are convenience functions that extends the basic iview 
    functionally about or/and make calls more transparent
    '''
    ###############################################################################        
 
    #%%             
    def set_cal_positions(self, cal_positions):
        """
        Sets the positions of the calibration locations
        cal_positions is a dict:  {1:[x,y],2:[x,y],....}
        """
        if cal_positions:
            for k in cal_positions.keys():
                self.change_calibration_point(k, cal_positions[k][0], cal_positions[k][1])    

     

    #%% 
    def set_begaze_trial_image(self, imname):
        '''
        imname - ex. 'testimage.jpg'
        The filename should not include a path
        '''
        
        # Skip the path if there is one
        filename  = os.path.split(imname)[1]
        
        # Get the file extension
        ext = os.path.splitext(imname)[1]
        
        # check extention is one of the supported ones
        assert(len([i for i in ['.png','.jpg','.jpeg','.bmp','.avi'] if ext == i]) > 0), "Filename not supported"
        self.send_image_message(imname)
        
    #%% 
    def set_begaze_mouse_click(self, which, x, y):
        ''' Make BeGaze understand that a mouse click has happened
        '''
        assert which in 'left' or which in 'right', 'SMITE: SMI BeGaze mouse press must be for ''left'' or ''right'' mouse button'

        self.send_image_message('UE-mouseclick {} x={} y={}'.format(which, x, y))  
        
    #%% 
    def set_begaze_key_press(self, string):
        '''  can use this to send any string into BeGaze event stream (do
        not know length limit). We advise to keep this short
        special format to achieve this
        '''
        self.send_image_message('UE-keypress {}'.format(string))

    #%%     
    def start_eye_image_recording(self, image_name, path):
        ''' Starts eye image recording
        Example: start_eye_image_recording('test',"c:\\eyeimages\\" )
        '''
        
        self.send_command(' '.join(["ET_EVB 1", image_name, path]))

            
    #%%             
    def stop_eye_image_recording(self):
        ''' Stops eye image recording
        '''
        self.send_command("ET_EVE")
               
     
    #%%
    def get_latest_sample(self):
        ''' Simulates gaze position with mouse
        ToDO use same struct as gaze data
        '''
        x, y = self.mouse.getPos()
        
        xy = np.array([[x, y]])
        mon = self.win.monitor
        # Convert to SMI-coordinate system
        if 'norm' in self.win.units:
            xy = helpers.psychopy2smi(xy, mon, units='norm')
        elif 'deg' in self.win.units:
            xy = helpers.psychopy2smi(xy, mon, units='deg')
        elif 'pix' in self.win.units:
            xy = helpers.psychopy2smi(xy, mon, units='pix')
           
        # Here put x and y values in struct
        x = xy[0][0]
        y = xy[0][1]
        self.sample.leftEye.gazeX = x
        self.sample.leftEye.gazeY  = y
        self.sample.rightEye.gazeX = x
        self.sample.rightEye.gazeY = y
        
        return self.sample
        
        
    #%% 
    def get_headbox_coordinates(self):
        ''' Get headbox coordinates
        '''
        return self.get_tracking_status()
        
    #%%              
    def increment_trial_number(self):
        ''' Increments trial number in iview X buffer.
        '''
        self.send_command("ET_INC")

    
    #%%  
    @WINFUNCTYPE(None, CSample)
    def sample_callback(sample):
        ''' Callback function for sample data
        '''
        # Append data to buffer
        self.buf.append(sample)
        
    #%%
    def consume_buffer_data(self):
        ''' Consume all samples '''
        return self.buf.get_all()
        
    #%%
    def peek_buffer_data(self):
        ''' Consume all samples '''
        return self.buf.peek()
        
    #%% 
    def start_buffer(self, sample_buffer_length=3):  
        
        Thread.__init__(self)
        
        # Initialize the ring buffer
        self.buf = helpers.RingBuffer(maxlen=sample_buffer_length)
        self.__stop = False
        self.start()   
        
    #%%             
    def run(self):
        # Called by the e.g., et.start()
        # Continously read data into the ringbuffer (convert to deg)
        while True:
            if self.__stop:        
                break
            
            # Get samples and store in ringbuffer  
            sample = self.get_latest_sample()
            
            self.buf.append(sample)
            time.sleep(0.01)        
            
    #%%             
    def record_eye_images(self,name = 'img', dur = 1, recorded_eye = 0):
        '''
        Records eye images (without overlays for dur s)
        recorded_eye = 0 actually means right eye (wrong in SDK)
        ''' 
        
        self.stop_recording() 
        self.set_tracking_parameter(recorded_eye,3,0)
        self.set_tracking_parameter(recorded_eye,4,0)
        self.set_tracking_parameter(recorded_eye,5,0)
        core.wait(0.1)
          
        self.start_eye_image_recording(name)
        core.wait(dur)
        self.stop_eye_image_recording()    
        
        self.set_tracking_parameter(recorded_eye,3,1)
        self.set_tracking_parameter(recorded_eye,4,1)
        self.set_tracking_parameter(recorded_eye,5,1)  
  
        
    #%%                         
    def enable_bilateral_filter(self):
        '''
        This API bilateral filter was implemented due to special human-computer
        interaction (HCI) application requirements. It smoothes gaze position data in EyeDataStruct::gazeX and
        EyeDataStruct::gazeY contained in SampleStruct, e.g. obtained by iV_GetSample. The gaze data filter
        can be disabled using iV_DisableGazeDataFilter      
        '''
        self.enable_gaze_data_filter()
        
    #%%             
    def disable_bilateral_filter(self):        
        '''
        Disables bilateral filter
        '''
        self.disable_gaze_data_filter()
                
        
    #%% 
    def delete_temp_idf_file(self):
        ''' Remove temp idf-files (otherwise the iview
            server complains that there are unsaved data)
        '''
        
        try:
            subprocess.Popen([(''.join(['del /F /S /Q /A "',
                                        self.constants.temp_folder_path,
                                        '\*.idf"']))])
        except NameError:
            print('Could not delete temp idf files')
            
    #%%     
    def de_init(self, close_et_server=False):
        
        self.disable_processor_high_performance_mode()
        self.disconnect()
            
        if close_et_server:
            self.quit_server()
            
    #%%             
    def average_data(self, average = False):
        '''
        Should  data be averaged across the eyes?    
        ''' 
        
        if average:
            self.configure_filter(filter_type=1, filter_action=1)
        else:
            self.configure_filter(filter_type=0, filter_action=1)
                                            
    

