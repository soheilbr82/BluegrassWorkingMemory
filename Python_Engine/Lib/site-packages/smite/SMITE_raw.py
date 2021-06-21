#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Load required packages 
from psychopy import core, event, misc
from iViewXAPI import*
from iViewXAPIReturnCodes import* 
import subprocess
import numpy as np
import helpers
import glob
import os
from scipy import misc
from ctypes import *

global buf # Used to keep data in ring buffer

# Numbers used by iView X for identify eye trackers
ET_server_dict = {'iViewX':0, 'iViewXOEM':1, 'iViewNG':2}
ET_device_dict = {'NONE':0, 'RED':1, 'REDm':2, 'RED250Mobile':2, 'HiSpeed':3,
                  'MRI':4, 'HED':5, 'Custom':7, 'REDn_Professional':8, 
                  'REDn_Scientific':8}

tracking_mode_dict = {'SMART_BINOCULAR':0, 'MONOCULAR_LEFT':1,
                      'MONOCULAR_RIGHT':2, 'BINOCULAR':3, 
                      'SMART_MONOCULAR':4}   

#%%    
        
class Connect(object):
    """ Basic functionally to communicate with and manage SMI eye trackers
    """
    def __init__(self, in_arg):
        '''
        Constructs an instance of the SMITE interface, with specified settings. 
        If settings is not provided, the name of an eye tracker should 
        be given, e.g., RED-m
        '''
        self.clock = core.Clock()
        self.connect_timeout = 30 # in seconds 
        
        # Define what's supported on the different eye tracker
        self.set_sampling_freq_allowed = True
        self.set_binocular_allowed = True
        self.geom_profile = False
        self.set_tracking_mode_allowed = False
        self.set_cal_positions_allowed = True # TODo
        self.enable_processor_high_performance = True

        # String, i.e., eye tracker name OR settings as argument?
        if isinstance(in_arg, str): # 3ye tracker name
            eye_tracker_name = in_arg
        else:                       # settings
            constants = in_arg
            eye_tracker_name = constants.eye_tracker_name
            
        if eye_tracker_name == 'REDm':
            import REDm as constants
            self.et_server_name = 'iViewXOEM'
            self.set_tracking_mode_allowed = True
            self.geom_profile = True
        elif eye_tracker_name == 'HiSpeed':
            import HiSpeed as constants
            self.enable_processor_high_performance_mode = False
            self.et_server_name = 'iViewX'
            self.set_binocular_allowed = False
            self.enable_processor_high_performance = False
        elif eye_tracker_name == 'RED':
            import RED as constants
            self.et_server_name = 'iViewX'
        elif eye_tracker_name == 'REDn':
            import REDn as constants
            self.et_server_name = 'iViewNG'
            self.set_tracking_mode_allowed = True
            self.geom_profile = True
        elif eye_tracker_name == 'REDn_Professional':
            self.et_server_name = 'iViewNG'
            self.set_tracking_mode_allowed = True
            self.geom_profile = True            
            import REDn_Professional as constants
        elif eye_tracker_name == 'REDn_Scientific':
            self.et_server_name = 'iViewNG'
            import REDn_Scientific as constants  
            self.set_tracking_mode_allowed = True
            self.geom_profile = True            
        elif eye_tracker_name == 'RED250mobile':
            self.et_server_name = 'iViewNG'
            import RED250mobile as constants  
            self.set_tracking_mode_allowed = True
            self.geom_profile = True
        else:
            print('Eye tracker not defined')
            core.quit()   
             
        self.constants = constants
        self.eye_tracker_name = eye_tracker_name
        
        print(self.et_server_name)
        
    #%%
    def init(self):
        ''' Connects to the eye tracker and initializes it according to the 
        specified settings
        '''        
        
        # Connect to eye tracker
        self.connect(self.constants.ip_listen, self.constants.port_listen,
                     self.constants.ip_send, self.constants.port_send)
                
        # Stop recording and clear buffer
        self.stop_recording()
        self.clear_recording_buffer()
        
        # Reset calibration points (also resets calibration)
        if self.constants.reset_calibration_points:
            self.reset_calibration_points()
                   
        # Set sampling frequency
        if self.set_sampling_freq_allowed:
            self.set_speed_mode(self.constants.sampling_freq)
                
        # Enable high performance mode
        if self.enable_processor_high_performance:
            self.enable_processor_high_performance_mode()
        
        # Select RED geometry profile
        if self.geom_profile:
            self.select_RED_geometry(self.constants.geom_profile)
        
        # Get system info 
        self.system_info = self.get_system_info()
        self.Fs = self.system_info['samplerate']
               
        # Quit if sampling rate is not the desired one
        if self.Fs != self.constants.sampling_freq:
            print('Sampling rate other than desired')
            core.quit()
            
        # Check that iview X agree that the desired eye tracker is connected
        eye_tracker_name_iview = self.system_info['iV_ETDevice']
        if ET_device_dict[self.eye_tracker_name] != eye_tracker_name_iview:
            print('Warning: iview thinks that you are using another eye tracker than the one you specified')        
             
        # Internal variable to keep track of whether samples 
        # are put into the buffer or not
        self.__buffer_active = False 
        
        # Remove temp idf-files (otherwise the iview
        # server complains that there are unsaved data)
        self.delete_temp_idf_file()
            
        if self.set_tracking_mode_allowed:
            self.set_tracking_mode(self.constants.track_mode)
            
        # Turn on of off data averaging
        self.average_data(average=self.constants.average_data)
        
        # Never allow the SDK to take control of the calibration keys
        self.set_use_calibration_key(0)
        
        # Enable of disable filters?
        if self.constants.filtering:
            self.enable_bilateral_filter()
        else:
            self.disable_bilateral_filter()
                        
        # Setup calibration parameters
        self.setup_calibration_parameters(autoaccept=self.constants.autoaccept,
                                          cal_method=self.constants.n_cal_points, 
                                          cal_speed=self.constants.cal_speed,
                                          screen = self.constants.screen)
     
    #%% 
    def abort_calibration(self):        
        ''' Aborts calibration
        All system supported
        '''
        res = iViewXAPI.iV_AbortCalibration()
        HandleError(res)    
        
    #%% 
    def abort_calibration_point(self):        
        ''' Aborts calibration point
        Supported systems: REDn, RED250 Mobile
        '''
        res = iViewXAPI.iV_AbortCalibrationPoint()
        HandleError(res)  

            #%%             
    def accept_calibration_point(self):
        ''' Wait for accept 
        All system supported
        '''        
        print('cal_point_accepted')
        res = iViewXAPI.iV_AcceptCalibrationPoint()
        HandleError(res)
        
    #%%
    def calibrate_iview(self):
        ''' Initiate calibration. Calibration parameters first need to 
        be set, see 'setup_calibration_parameters'
        All system supported        
        ''' 
        res = iViewXAPI.iV_Calibrate()
        HandleError(res)       
        
    #%%                     
    def change_calibration_point(self, number, positionX, positionY):
        ''' Change calibration point 'number' to a new position (positionX, positionY)
        All system supported (WARNING: should not be done on the remotes unless
        you REALLY know what you're doing. So don't do it.)       
        This has to be done before the calibration process is started.
        
        Args:
            number - calibration point number (int)
            positionX - x position of new point (pixels)
            positionY - y position of new point (pixels)
            
        Origo of coordinate system is the uppler left corner of screen.
        '''
        res = iViewXAPI.iV_ChangeCalibrationPoint(number, positionX, positionY)
        HandleError(res)              
        
    #%%
    def clear_aoi(self):
        ''' Removes all trigger AOIs
        Not supported. Use your own code and data from the buffer instead
        Supported systems: RED, RED-m, HiSpeed 
        ''' 
        
        res = iViewXAPI.iV_ClearAOI() 
        HandleError(res)        
        
    #%%             
    def clear_recording_buffer(self):
        ''' Clears recording buffer from all recorded data
        Supported systems: all
        '''         
        res = iViewXAPI.iV_ClearRecordingBuffer() 
        HandleError(res)
        
        
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
        
        filter_status = c_void_p(0)             
        res = iViewXAPI.iV_ConfigureFilter(c_int(filter_type), 
                c_int(filter_action), byref(filter_status))
        HandleError(res)
        
        #print(filter_type, filter_action, res)
        
        return filter_status

        
    #%%     
    def connect(self, ip_listen, port_listen, ip_send, port_send, 
                connect_timeout=30):
        ''' Connect to eye tracker server
        Supported systems: all 
        
        Args:
            ip_listen       - listen ip address
            port_listen     - list port number
            ip_send         - send ip address
            port_send       - send port number
            connect_timeout - keep trying to connect for 'connect_timeout' s
        '''
        connected = False
        self.clock.reset()
        while not connected and self.clock.getTime() < connect_timeout:
            
            if not ip_send == ip_listen:
                res = iViewXAPI.iV_Connect(c_char_p(ip_listen.encode('ascii')),
                                           c_int(port_listen),
                                           c_char_p(ip_send.encode('ascii')),
                                           c_int(port_send))
            else:
                res = iViewXAPI.iV_ConnectLocal()
                
                                       
            # If eye tracker is not started, start it and try to connect again
            if res != 1:
                
                HandleError(res)
                #print(ET_server_dict[self.et_server_name])
                try:
                    # Start eye tracker server
                    self.start_iview_server(ET_server_dict[self.et_server_name])
                except:
                    print('Failed to connect. Trying again')
                    
                core.wait(10)
            elif res == 1:
                connected = True
        
        if not connected:
            print('Connection to eye tracker failed after repeated attempts to connect')
            core.quit()  
        
    #%% 
    def continue_eye_tracking(self):
        '''
        Wakes up and enables the eye tracking application from suspend mode to continue processing gaze
        data. The application can be set to suspend mode by calling iV_PauseEyetracking        
        
        Supported systems: all but RED and HiSpeed

        '''
        res = iViewXAPI.iV_ContinueEyeTracking()
        HandleError(res)        
        
    #%% 
    def continue_recording(self, msg):
        '''
        Continues gaze data recording. iV_ContinueRecording does not return until gaze recording is continued.
        Before it can be continued, the data needs to be paused using. iV_PauseRecording. Additionally this
        function allows a message to be stored inside the idf data buffer.        
        
        Supported systems: all
        '''       
        
        res = iViewXAPI.iV_ContinueRecording(msg)
        HandleError(res)              
        
    #%% 
    def define_aoi(self, aoi_data):
        '''
        Defines an AOI. The API can handle up to 20 AOIs
        
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            aoi_data - struct, see SDK manual for description
        '''     
        
        res = iViewXAPI.iV_DefineAOI(aoi_data)
        HandleError(res)          

    #%% 
    def define_aoi_port(self, port):
        '''
        Selects a port for sending out TTL trigger
        
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            port - int
        '''  
        
        res = iViewXAPI.iV_DefineAOIPort(c_int(port))
        HandleError(res)             
        
    #%% 
    def delete_red_geometry(self, profile):
        '''
        Deletes the geometry setup with the given profile name. It is not possible 
        to delete a geometry profile if it is currently in use. 
        See chapter Setting up RED Geometry in the iView X SDK Manual.
        
        Supported systems: all but HiSpeed
        
        Args:
            profile - string with profile name
        '''              
        res = iViewXAPI.iV_DeleteREDGeometry(profile)
        HandleError(res)
        
    #%% 
    def disable_aoi(self, aoi_name):
        '''
        Disables all AOIs with the given name.
        
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            port - int
        '''  
        
        res = iViewXAPI.iV_DisableAOI(c_char(aoi_name))
        HandleError(res)             
        
    #%% 
    def disable_aoi_group(aoi_group):
        '''
        Disables an AOI group
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            port - int
        '''  
        
        res = iViewXAPI.iV_DisableAOIGroup(c_char(aoi_group))
        HandleError(res)          
        
    #%% 
    def disable_gaze_data_filter(self):
        '''
        Disables the raw data filter. The gaze data filter can be enabled using 
        iV_EnableGazeDataFilter.        
        Supported systems: all 

        '''   
        res = iViewXAPI.iV_DisableGazeDataFilter()
        HandleError(res)
        
      
        
    #%% 
    def disable_processor_high_performance_mode(self):
        '''
        Disables a CPU high performance mode allowing the CPU to reduce the performance.
        Supported systems: all but RED and Hi-Speed
        '''
        res = iViewXAPI.iV_DisableProcessorHighPerformanceMode()
        HandleError(res)	           
  
    #%% 
    def disconnect(self):
        ''' Disconnects the eye tracker 
        Supported systems: all
        '''
        res = iViewXAPI.iV_Disconnect() 
        HandleError(res)    
        
    #%% 
    def enable_aoi(self, aoi_name):
        '''
        Enables all AOIs with the given name
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            aoi_name - string with name of aoi
        '''  
        
        res = iViewXAPI.iV_EnableAOI(c_char(aoi_name))
        HandleError(res)             
        
    #%% 
    def enable_aoi_group(self, aoi_group):
        '''
        Disables an AOI group
        Supported systems: all but RED-n and RED250 mobile.
        
        Args:
            aoi_group - string with name of aoi group
        '''
        
        res = iViewXAPI.iV_EnableAOIGroup(c_char(aoi_group))
        HandleError(res)   
        
    #%%                         
    def enable_gaze_data_filter(self):
        '''
        This API bilateral filter was implemented due to special human-computer
        interaction (HCI) application requirements. It smoothes gaze position data in EyeDataStruct::gazeX and
        EyeDataStruct::gazeY contained in SampleStruct, e.g. obtained by iV_GetSample. The gaze data filter
        can be disabled using iV_DisableGazeDataFilter   
        '''
        res = iViewXAPI.iV_EnableGazeDataFilter() 
        HandleError(res)   
        
        
    #%% 
    def enable_processor_high_performance_mode(self):
        '''
        Enables a CPU high performance mode allowing the CPU to reduce the performance.
        Supported systems: all but RED and Hi-Speed
        '''
        res = iViewXAPI.iV_EnableProcessorHighPerformanceMode()
        HandleError(res)	    
        
    #%%
    def get_accuracy(self, visualization = 0):
        ''' Get accuracy. Only possible after a successful validation
        If the parameter visualization is set to 1 the accuracy
        data will be visualized in a dialog window.
        
        Args:
            visualization - int
            
        Returns:
            accuracy values for left and right eyes
            
        ''' 

        res = iViewXAPI.iV_GetAccuracy(byref(accuracyData), visualization)
        HandleError(res)	
        
        return (accuracyData.deviationLX, accuracyData.deviationLY,
               accuracyData.deviationRX, accuracyData.deviationRX)

    #%%         
    def get_accuracy_image(self, fname=None):
        ''' Returns validation screen image and optinally save it to disk
        
        Args:
            fname - name of image to be saved to disk, e.g., 'im.png'
            
        Returns:
            im - image as n x m x 3 numpy array
        '''
        
        # update imageData with the most recent accuracy image        
        res = iViewXAPI.iV_GetAccuracyImage(byref(imageData))
        
        # Convert imageData.imageBuffer to something understandable
        ac = np.array(imageData.imageBuffer[:imageData.imageSize], 'c')
        ac_as_int = ac.view(np.uint8)
        ac_as_int = ac_as_int[:imageData.imageSize]
        
        # Make background gray instead of black
        ac_as_int[ac_as_int == 0] = 128
        im = np.reshape(ac_as_int, [imageData.imageHeight, imageData.imageWidth, 3]) 
        
        # Save image to disk if a file name is given
        if fname:
            misc.imsave(fname, im)
            core.wait(0.1)
            
        return im
        
    #%% 
    def get_aoi_output_value(self):
        '''
        Returns the current AOI value.
        Supported systems: all 
        
        Returns:
            aoiOutputValue - int
        '''  
        
        res = iViewXAPI.iV_getAOIOutputValue(byref(aoiOutputValue))
        HandleError(res)     
        
        return aoiOutputValue
        
    #%%
    def get_calibration_parameter(self):
        ''' Updates stored calibrationData information with currently selected 
            parameters.
        Supported systems: RED-n and RED250 Mobile 
        
        Returns:
            calibrationData - structure containing information about calibration
        '''
        
        res = iViewXAPI.iV_getCalibrationParameter(byref(calibrationData))
        HandleError(res)           
        return calibrationData
        
    #%%
    def get_calibration_point(self, calibration_point_number):
        ''' Delivers information about a calibration point.
        Supported systems: all
        
        Args:
            calibration_point_number - number of calibration point
        
        Returns:
            calibrationPoint - struct with info about calibration point
            Contains number (int), positionX (int), and positionY (int)
        '''
        
        res = iViewXAPI.iV_getCalibrationPoint(c_int(calibration_point_number),
                                               byref(calibrationPoint))
        HandleError(res)           
        return calibrationPoint   
        
    #%%
    def get_calibration_quality(self, calibration_point_number):
        ''' Delivers fixation quality information about a calibration point. 
        If the passed parameter left or right is NULL, no data will be returned
        Supported systems: RED-n and RED250 Mobile 
        
        Args:
            calibration_point_number - number of calibration point        
        '''      
        
        res = iViewXAPI.iV_getCalibrationPointQuality(c_int(calibration_point_number),
                                               byref(left), byref(right))
        HandleError(res)           
        return left, right          
        
    #%%
    def get_calibration_quality_image(self):
        ''' 
        Same functionally as get_accuracy_image
        Supported systems: RED-n and RED250 Mobile 

        Returns:
            imageData - 
        '''   
        
        res = iViewXAPI.iV_getCalibrationPoint(byref(imageData))
        HandleError(res)           
        return imageData           
        
    #%%
    def get_calibration_status(self):
        ''' Updates calibrationStatus information. 
        The client needs to be connected to the iView eye tracking server.
        Supported systems: all        
        ''' 
        
        res = iViewXAPI.iV_getCalibrationStatus(byref(calibrationStatus))
        HandleError(res)           
        return calibrationStatus         

    #%%
    def get_current_calibration_point(self):
        ''' Updates data in currentCalibrationPoint with the current calibration 
        point position
        Supported systems: all        
        '''
        res = iViewXAPI.iV_GetCurrentCalibrationPoint(byref(currentCalibrationPoint))
        HandleError(res)       
        
        return res, currentCalibrationPoint

    #%% 
    def get_current_RED_geometry(self):
        '''
        Supported systems: all but HiSpeed
        '''        
        res = iViewXAPI.iV_GetCurrentREDGeometry(byref(redGeometry))
        HandleError(res)
                    
        return redGeometry
    
    #%% 
    def get_current_time_stamp(self):
        ''' Provides the current eye tracker timestamp in microseconds
        Supported systems: all
        '''        
        res = iViewXAPI.iV_GetCurrentTimestamp(byref(currentTimestamp))
        HandleError(res)
                    
        return currentTimestamp  
    
    #%%
    def get_device_name(self):
        ''' Queries the device name information of the connected device.
        Supported systems: all but RED and HiSpeed
        '''                
        res = iViewXAPI.iV_GetDeviceName(byref(deviceName))
        HandleError(res)
        
        return deviceName    
    
    #%%
    def get_event(self):
        ''' Updates data from eventDataSample with current event data.
        Supported systems: all but RED-n professional
        '''                
        res = iViewXAPI.iV_GetEvent(byref(eventDataSample))
        HandleError(res)
        
        return eventDataSample        
    
    #%%                     
    def get_eye_image(self):
        ''' Updates imageData with current eye image (format: monochrome 8bpp).
        Supported systems: ToDo
        '''   
        res = iViewXAPI.iV_GetEyeImage(byref(imageData)) 
        #core.wait(0.)
        if res == 1:
            
            # Convert image to 1-d array
            ac = np.array(imageData.imageBuffer[:imageData.imageSize], 'c')
            ac_as_int = ac.view(np.uint8)
            ac_as_int = ac_as_int[:imageData.imageSize]
            
            # Reshape to 2-d image and normalize values to [-1, 1]
            im = np.zeros(imageData.imageSize)
            im[:np.shape(ac_as_int)[0]] = ac_as_int
            im = np.reshape(im, [imageData.imageHeight, imageData.imageWidth])
            
            #np.save('eye_im', im)
            
            im = np.fliplr((im / float(im.max()) * 2) - 1)
            #print(imageData.imageHeight, imageData.imageWidth, 3)

            im_res = [imageData.imageHeight, imageData.imageWidth]
            
        else:
            im_res = [self.constants.eye_image_size[0], self.constants.eye_image_size[1]]
            im = np.zeros([self.constants.eye_image_size[0], self.constants.eye_image_size[1]])
            HandleError(res)


            
        # Fit image to a 512x512 container (must be power of 2)
        # 
        if self.constants.eye_tracker_name == 'HiSpeed':
            im_sz = 1024
        else:
            im_sz = 512
            
        # Scale the eye image
        #print(imageData.imageHeight, imageData.imageWidth, np.shape(im))
        im_final = np.zeros([im_sz, im_sz])
        row_idx = (im_sz - im_res[0]) / 2
        col_idx = (im_sz - im_res[1]) / 2
        im_final[int(row_idx):int(row_idx+im_res[0]),
                 int(col_idx):int(col_idx+im_res[1])] = np.rot90(im, 2)
        
        return im_final, res

    #%%
    def get_feature_key(self):
        ''' Gets the device specific feature key. Used for RED-OEM, RED250mobile and REDn devices only
        Supported systems: RED-n and RED250 Mobile
        '''                
        
        res = iViewXAPI.iV_GetFeatureKey(byref(featureKey))
        HandleError(res)
        
        return featureKey        

    #%%
    def get_gaze_channel_quality(self):
        ''' Retrieve gaze quality data. Fills qualityData with validated accuracy results. Before quality data is
        accessible the system needs to be validated with iV_Validate
        Supported systems: RED-n and RED250 Mobile
        
        ''' 
        
        res = iViewXAPI.iV_GetGazeChannelQuality(byref(qualityData))
        HandleError(res)
        
        return qualityData            
        
        
    #%%
    def get_recording_state(self):
        ''' Queries the recording state of the eye tracking server. 
        This function can be used to check if the eye
        tracking server is currently performing a recording.
        Supported systems: RED-n and RED250 Mobile
        '''             
        
        res = iViewXAPI.iV_GetRecordingState(byref(recordingState))
        HandleError(res)
        
        return recordingState

    #%% 
    def get_RED_geometry(self, profile_name):
        ''' Gets the geometry data of a requested profile without selecting them.
        Supported systems: all but HiSpeed
        '''                
        res = iViewXAPI.iV_GetREDGeometry(profile_name, byref(redGeometry))
        HandleError(res)
                    
        return redGeometry    


    #%%             
    def get_sample(self):
        ''' Updates data in sampleData with current eye tracking data.
        Supported systems: all
        ''' 
        res = iViewXAPI.iV_GetSample(byref(sampleData))
        HandleError(res)
        return sampleData 
    
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
        
        res = iViewXAPI.iV_GetSample(byref(serialNumber))
        HandleError(res)
        return serialNumber     
    
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
        
        res = iViewXAPI.iV_GetSpeedModes(byref(speedModes))
        HandleError(res)
        return  speedModes       
    
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
    
        res = iViewXAPI.iV_GetSystemInfo(byref(systemData))
        HandleError(res)
        
        system_info = {'API_Buildnumber':systemData.API_Buildnumber,
        'API_Buildnumber':systemData.API_Buildnumber,
        'API_MajorVersion':systemData.API_MajorVersion,
        'API_MinorVersion':systemData.API_MinorVersion,
        'iV_Buildnumber':systemData.iV_Buildnumber,
        'iV_ETDevice':systemData.iV_ETDevice,
        'iV_MajorVersion':systemData.iV_MajorVersion,
        'iV_MinorVersion':systemData.iV_MajorVersion,
        'samplerate':systemData.samplerate}
        print('hej')
        print(systemData.iV_ETDevice)
        return system_info  
    
    #%%     
    def get_tracking_mode(self):
        ''' Get eye tracking mode (see set_tracking_mode)
        ''' 
        res = iViewXAPI.iV_GetTrackingMode(byref(mode))
        HandleError(res)
        
        return mode    
    
    #%%         
    def get_tracking_monitor(self):
        ''' Returns tracking monitor
        
        The tracking monitor image depicts the positions of both eyes and shows notification arrows 
        if the participant is not properly positioned infront of the eye tracker. 
        The tracking monitor is useful to validate the positioning before and 
        during a recording session.  
        
        Supported systems: all but HiSpeed                   
        '''
        
        # update imageData with the most recent accuracy image        
        res = iViewXAPI.iV_GetTrackingMonitor(byref(imageData))
        
        # Convert imageData.imageBuffer to something understandable
        ac = np.array(imageData.imageBuffer[:imageData.imageSize], 'c')
        ac_as_int = ac.view(np.uint8)
        ac_as_int = ac_as_int[:imageData.imageSize]
        #print(imageData.imageHeight, imageData.imageWidth)
        
        # ValueError: total size of new array must be unchanged
        if len(ac_as_int) == imageData.imageHeight * imageData.imageWidth * 3:
            im = np.reshape(ac_as_int, [imageData.imageHeight, imageData.imageWidth, 3])
            im = (im / float(im.max()) * 2) - 1
            im = im[:, :, ::-1]
            im[im < 0] = 0
            im[0, 0, 0] = -1
            im = np.fliplr(im)
        else:
            im = np.zeros((self.constants.eye_image_size[0], self.constants.eye_image_size[1], 3))
            res = 2

        return im, res   
    
    #%% 
    def get_tracking_status(self):
        ''' Updates trackingStatus with current tracking status.
        This function can be used to get the current eye positions.
        
        Supported systems: all 
        
        '''
        res =  iViewXAPI.iV_GetTrackingStatus(byref(trackingStatus))
        HandleError(res)
        return trackingStatus      
    
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
        
        enableKeys = c_int(0)
        res = iViewXAPI.iV_GetUseCalibrationKeys(byref(enableKeys))
        HandleError(res)
        return enableKeys   
    
    
    #%%
    def hide_accuracy_monitor(self):
        ''' Hides accuracy monitor window which can be opened by iV_ShowAccuracyMonitor.
        Supported systems: all
        '''     
        
        res = iViewXAPI.iV_HideAccuracyMonitor()
        HandleError(res)        
        
    #%%
    def hide_eye_image_monitor(self):
        ''' Hides eye image monitor window which can be opened by iV_ShowEyeImageMonitor.
        Supported systems: all but RED-n professional
        '''     
        
        res = iViewXAPI.iV_HideEyeImageMonitor()
        HandleError(res)         

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
        
        res = iViewXAPI.iV_HideTrackingMonitor()
        HandleError(res)           
        
    #%% 
    def is_connected(self):
        ''' Checks if connection to iView eye tracking server is still established.
        Supported systems: all 
        
        Returns:
            res - 1 if intended functionality has been fulfilled
                  0 if no connection established
        
        '''
        
        res = iViewXAPI.iV_IsConnected()
        HandleError(res)
        return res
    
    #%%         
    def load_calibration(self, name):
        ''' Loads a previously saved calibration. A calibration has to be saved by using iV_SaveCalibration.
        
        Supported systems: all 
        
        '''        
        res = iViewXAPI.iV_LoadCalibration(c_char_p(name.encode('ascii')))
        HandleError(res)    
        
    #%%         
    def log(self, msg):
        ''' Writes logMessage into log file
        
        Supported systems: all 
        
        '''        
        res = iViewXAPI.iV_Log(c_char_p(msg.encode('ascii')))
        HandleError(res)       
        
    #%%
    def pause_eye_tracking(self):
        ''' Suspend the eye tracking application and disables calculation of gaze data. 
        The application can be reactivated by calling iV_ContinueEyetracking.
        Supported systems: all but RED and HiSpeed
        '''     
        
        res = iViewXAPI.iV_PauseEyeTracking()
        HandleError(res)          
        
    #%%
    def pause_recording(self):
        ''' Pauses gaze data recording. iV_PauseRecording does not return until 
        gaze recording is paused.
        Supported systems: all 
        '''    
        
        res = iViewXAPI.iV_PauseRecording()
        HandleError(res)         
        
    #%% 
    def quit_server(self):
        ''' Disconnects and closes iView eye tracking server. 
        After this function has been called no other function
        or application can communicate with iView eye tracking server.
        '''
        
        res = iViewXAPI.iV_Quit()  
        HandleError(res)
        
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
        
        res = iViewXAPI.iV_RecalibrateOnePoint(c_int(calibration_point_number))  
        HandleError(res)        
        
        
    #%%
    def release_aoi_port(self):
        ''' Releases the port for sending TTL trigger.
        Supported systems: all but RED-n and RED250 Mobile 
        '''
        
        res = iViewXAPI.iV_ReleaseAOIPort()  
        HandleError(res)            
        
    #%%
    def remove_aoi(self, name):
        ''' Removes all AOIs with the given name.
        Supported systems: all but RED-n and RED250 Mobile 
        '''   

        res = iViewXAPI.iV_RemoveAOI()  
        HandleError(res)    
        
    #%%                         
    def reset_calibration_points(self):           
        ''' Resets the positions of the calibration points
        Supported systems: all 
        
        '''         
        res = iViewXAPI.iV_ResetCalibrationPoints()
        HandleError(res)        
        
    #%%    	
    def save_calibration(self, name):
        ''' Saves a calibration with a custom name. To save a calibration it 
        is required that a successful calibration already has been completed.
        
        Supported systems: all 
        
        '''
        res = iViewXAPI.iV_SaveCalibration(c_char_p(name.encode('ascii')))
        HandleError(res)      
        
    #%%             
    def save_data(self, filename, description = "", 
                   user = None, append_version=True):
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
            append_version - append version number to file if exists (e.g., _1, _2, etc)
        
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
            
        # If the filename already exists, append _x
        files = glob.glob(path + os.sep + '*.idf')
        
        i = 1
        filename_ext = ''
        while True:
            
            # Go through the files and look for a match
            filename_exists = False
            for f in files:
                f_temp = f.split('\\')[-1][:-4]
                
                # if the file exists
                if filename + filename_ext == f_temp:
                    if not append_version:
                        raise ValueError('Warning! Filename already exists')
                    else: # append '_i to filename
                        filename_ext = '_' + str(i)          
                        filename_exists = True
                        i += 1
                    
            # If we've gone through all files without
            # a match, we ready!
            if not filename_exists:
                 break
             
        # Add the new extension the the filename        
        filename = os.sep.join([path, filename + filename_ext + ext])
        
        # If two computer setup (TODO)
#        if not ip_send == ip_listen:
#            # Two computer setup: file gets saved on eye-tracker
#            # computer (do so with without path info and allowing
#            # overwrite). Transfer the file using the
#            # FileTransferServer running on the remote machine. NB:
#            # this seems to only work when iView is running on the
#            # remote machine.
#            
#            # 1: connect to file transfer server
#            # 1a: request FileTransferServer.exe's version (always
#            #     happens when experiment center is just started)            
#            pass
#        else:
#            pass
#            print(filename)
        res = iViewXAPI.iV_SaveData(c_char_p(filename.encode('ascii')), 
                                    c_char_p(description.encode('ascii')), 
                                    c_char_p(user.encode('ascii')), 
                                    0) # Never overwrite existing file with the same name
        HandleError(res)       
        
    #%% 
    def select_RED_geometry(self, profile):
        ''' Selects a predefined geometry profile. 
        
        Supported systems: all but HiSpeed 
        
        '''
        print(profile)
        res = iViewXAPI.iV_SelectREDGeometry(c_char_p(profile.encode('ascii')))
        HandleError(res)   
        assert(res==1), "RED geometry profile does not exist"
        
        
    #%%
    def send_command(self, cmd):
        ''' Sends a remote command to iView eye tracking server. 
        Please refer to the iView X help file for further information about remote commands.
        
        Supported systems: all 
        '''
        res = iViewXAPI.iV_SendCommand(cmd)
        HandleError(res)       
        
    #%%             
    def send_image_message(self, msg):
        ''' Sends a text message to iView X idf recording data file. 
        If the etMessage has the suffix ".jpg", ".bmp",
        ".png", or ".avi" BeGaze will separate the data buffer 
        automatically into according trials.
        
        Supported systems: all 
        '''
        res = iViewXAPI.iV_SendImageMessage(c_char_p(msg.encode('ascii')))
        HandleError(res)    
        
    #%%
    def set_aoi_hit_callback(self, callback_function):
        ''' Sets a callback function for the AOI hit functions.
        Supported systems: all but RED-n and RED250 Mobile
        
        '''
        res = iViewXAPI.iV_SetAOIHitCallback(callback_function)
        HandleError(res)         
        
    #%%
    def set_calibration_callback(self, callback_function):
        ''' Sets a callback function for the AOI hit functions.
        Supported systems: All
        '''           
        
        res = iViewXAPI.iV_SetCalibrationCallback(callback_function)
        HandleError(res)              
        
    #%%
    def set_connection_timeout(self, time):
        ''' Defines a customized timeout for how long iV_Connect tries to 
        connect to iView eye tracking server.
        Supported systems: all but RED-n professional 
        '''          
        
        res = iViewXAPI.iV_SetConnectionTimeout(time)
        HandleError(res)   

    #%%
    def set_event_callback(self, callback_function):
        ''' Sets a callback function for the event data. 
        The function will be called if a real-time detected fixation has
        been started or ended.
        Supported systems: all but RED-n professional 
        '''          
        
        res = iViewXAPI.iV_SetEventCallback(callback_function)
        HandleError(res)     
        
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
        
        res = iViewXAPI.iV_SetLicense(callback_function)
        HandleError(res)     
        
    #%%
    def set_licence(self, key):
        ''' Sets the customer license (required only for OEM devices!).
        Supported systems: RED-n and RED-n scientific
        '''             
        
        res = iViewXAPI.iV_SetLicense(key)
        HandleError(res)     
        
    #%%
    def set_logger(self, log_level=1, filename='iv_logfile'):
        ''' Sets the customer license (required only for OEM devices!).
        
        ToDo: What log levels are there and what do they mean?
        Supported systems: all 
        
        '''             
        
        res = iViewXAPI.iV_SetLogger(key)
        HandleError(res)        
        
    #%%
    def set_resolution(self, stimulus_width, stimulus_height):
        ''' Sets the customer license (required only for OEM devices!).
        
        Defines a fixed resolution independent to the screen resolution of 
        chosen display device defined in iV_-SetupCalibration function.
        
        Could be useful when using real-time data with a screen with low resolution.
        Supported systems: all 
        
        '''             
        
        res = iViewXAPI.iV_SetResolution (c_int(stimulus_width), 
                                          c_int(stimulus_height))
        HandleError(res)   
        
    #%%
    def set_RED_geometry(self, setup_mode = 0, 
                                    monitor_size = 22,
                                    setup_name = 'test',
                                    stim_x=0,
                                    stim_y=0,
                                    stim_height_over_floor=0,
                                    red_height_over_floor=0,
                                    red_stim_dist=0,
                                    red_incl_angle=0,
                                    red_stim_dist_height=0,
                                    red_stim_dist_depth=0):
        ''' Define the eye trackers stand alone and monitor integrated geometry
        
        The dict should included
        
        Supported systems: all but HiSpeed
        
        int monitorSize:        monitor size [inch] can be set to 19 or 22 used if redGeometry is 
                                set to monitorIntegrated only
        enum REDGeometryEnum redGeometry: defines which parameter is used. Can be 'monitorIntegrated' (0) or 'standalone'(1)
        
        int redHeightOverFloor: distance floor to eye tracking device [mm] used 
                                if redGeometry is set to standalone only
        int redInclAngle:       eye tracking device inclination angle [degree] used if redGeometry
                                is set to standalone only
        int redStimDist:        distance eye tracking device to stimulus screen [mm] used if red-
                                Geometry is set to standalone only
        int redStimDistDepth:   horizontal distance eye tracking device to stimulus screen [mm]
                                used if redGeometry is set to standalone only
        int redStimDistHeight:  vertical distance eye tracking device to stimulus screen [mm] used
                                if redGeometry is set to standalone only
        char setupName:         name of the profile used if redGeometry is set to standalone only
        int stimHeightOverFloor:distance floor to stimulus screen [mm] used if redGeometry is set
                                to standalone only
        int stimX:              horizontal stimulus calibration size [mm] used if redGeometry is
                                set to standalone only
        int stimY:              vertical stimulus calibration size [mm] used if redGeometry is set
                                to standalone only        
                                    
        '''      
        
        redGeometry = CREDGeometry(setup_mode, 
                                    monitor_size,
                                    setup_name,
                                    stim_x,
                                    stim_y,
                                    stim_height_over_floor,
                                    red_height_over_floor,
                                    red_stim_dist,
                                    red_incl_angle,
                                    red_stim_dist_height,
                                    red_stim_dist_depth)
                                    
        res = iViewXAPI.iV_SetREDGeometry(redGeometry)
        self.geom = self.get_current_RED_geometry()
        HandleError(res)           
        print(res)
    #%%
    def set_sample_callback(self, function_name):
        ''' Sets a callback function for the raw sample data. 
        The function will be called if iView eye tracking server
        has calculated a new data sample.
        Attention: Algorithms with high processor usage and long calculation 
        time should not run within this callback due to a higher probability of data loss
        Supported systems: all 
       
        '''             
        
        res = iViewXAPI.iV_SetSampleCallback(self.function_name)
        HandleError(res)    
        
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
            res = iViewXAPI.iV_SetSpeedMode(c_int(samplingrate))
            HandleError(res) 
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
            
            res = iViewXAPI.iV_SetTrackingMode(tracking_mode_dict[mode])
            HandleError(res)
        else:
            print("WARNING: set_tracking_mode is not supported on this eye tracker")          
            
    #%%
    def set_tracking_monitor_callback(self, function_name):
        ''' Sets a callback function for the tracking monitor image data. 
        The function will be called if a new tracking
        monitor image was calculated. The image format is BGR 24bpp
        Supported systems:  all but HiSpeed
        '''    

        res = iViewXAPI.iV_SetTrackingMode(function_name)
        HandleError(res)
        
        
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
        res = iViewXAPI.iV_SetTrackingParameter(c_int(eye_type), 
                                                c_int(parameter_type),
                                                c_int(activate))
        HandleError(res)   
        
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
        
        calibrationData = CCalibration(cal_method,
                                       0, # Always use Psychopy for visualization
                                       screen,
                                       cal_speed,
                                       autoaccept,
                                       fg_color,
                                       bg_color,
                                       target_shape,
                                       target_size,
                                       b"")
        res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
        print('CCdata {}'.format(res))
        HandleError(res)        
        
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
        res = iViewXAPI.iV_SetupDebugMode(c_int(enable_debug_mode))
        HandleError(res)            
        
    #%%
    def setup_ltp_recording(self, port_name, enable_recording):
        '''Enables or disables the LPT signal recording functionality. 
        Not Supported. 
        '''     
        
        res = iViewXAPI.iV_SetupLtpRecording(c_char(port_name), c_int(enable_recording))
        HandleError(res)                 
            
    #%%
    def set_use_calibration_key(self, mode):
        ''' Sets and resets the interaction keys during the calibration and validation process.
        See get_use_calibration_key
        '''
        res = iViewXAPI.iV_SetUseCalibrationKeys(c_int(mode))
        HandleError(res)         
        
    #%%
    def show_accuracy_monitor(self):
        '''The validated accuracy results will be visualized in a separate window. 
        Before the image can be drawn the calibration needs to be performed with 
        iV_Calibrate and validated with iV_Validate.
        Supported systems: all
        '''      
        res = iViewXAPI.iV_ShowAccuracyMonitor()
        HandleError(res)            
        
    #%%
    def show_eye_image_monitor(self):
        '''Visualizes eye image in a separate window while the participant is 
        beeing tracked (equal to image obtained with iV_GetEyeImage).
        Supported systems: all but RED-n professional and RED-m mx
        '''     
        
        res = iViewXAPI.iV_ShowEyeImageMonitor()
        HandleError(res)         
        
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
        
        res = iViewXAPI.iV_ShowTrackingMonitor()
        HandleError(res)       

    #%% 
    def start_iview_server(self, et_application):
        '''Starts the iView eye tracking server application. Depending on the PC, 
        it may take several seconds to start the iView eye tracking server application. 
        The connection needs to be established separately using iV_Connect. 
        The connection timeout can be extended using iV_SetConnectionTimeout.
        
        Supported systems: all 
        '''               
        print(et_application)
        res = iViewXAPI.iV_Start(c_int(et_application))
        HandleError(res)
        
    #%%             
    def start_recording(self):
        ''' Starts gaze data recording
        Supported systems: all
        '''
        res = iViewXAPI.iV_StartRecording()
        HandleError(res)        
        
    #%%             
    def stop_recording(self):
        ''' Stops gaze data recording
        Supported systems: all
        '''
        res = iViewXAPI.iV_StopRecording()
        HandleError(res)     
        
    #%%
    def test_ttl(self, value):
        '''Sends a TTL value to defined port. Define a port with iV_DefineAOIPort
        Supported systems: all
        '''
        res = iViewXAPI.iV_TestTTL(c_int(value))
        HandleError(res)   

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
        res = iViewXAPI.iV_Validate()
        HandleError(res)	
        
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
        ''' Gets most recent gaze sample
        '''
        #pickle.dump(self.get_sample(), open( "sample.p", "wb" ) )
        
        return self.get_sample()
        
        
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
        global buf
        buf.append(sample)
    #%%
    def consume_buffer_data(self):
        ''' Get data from the online buffer. The returned samples are removed 
        from the buffer
        '''
        return buf.get_all()
        
    def peek_buffer_data(self):
        ''' Get data from the online buffer. The returned samples remain in 
        the buffer
        '''
        return buf.peek()
        
        
    def clear_buffer_data(self):
        ''' Clears buffer. 
        '''
        buf.clear()
    #%% 
    def start_buffer(self, sample_buffer_length=3):
        '''Start recording eye-movement data into buffer for online use
        
        Args:
            sample_buffer_length - size of buffer in samples
        '''
        
        # Initialize the ring buffer
        global buf
        buf = helpers.RingBuffer(maxlen=sample_buffer_length)
        print(buf)
        #print(buf, type(buf))
        self.__buffer_active = True
        
        # Set callback (starts reading samples)
        #self.set_sample_callback('sample_callback')
        res = iViewXAPI.iV_SetSampleCallback(self.sample_callback)
        
    #%% 
    def stop_buffer(self):
        '''Stops sample buffer''' 
        
        self.__buffer_active = False
        
        # Set callback to None
        res = iViewXAPI.iV_SetSampleCallback(None)     
            
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
            subprocess.Popen('del /F /S /Q /A r"C:\\ProgramData\\SMI\\iView X\\temp\\*.idf"') # RED-m
            subprocess.Popen('del /F /S /Q /A r"C:\\ProgramData\\SMI\\TempRemoteRecordings\\*.idf"') # RED NG


        except:
            print('Could not delete temp idf files')
            
    #%%     
    def de_init(self, close_et_server=False):
        ''' Close connection to the eye tracker and clean up
        Args:
            close_et_server - closes the eye tracker server application
        '''
        
        self.disable_processor_high_performance_mode()
        self.disconnect()
            
        if close_et_server:
            self.quit_server()
            
    #%%             
    def average_data(self, average = False):
        ''' Average data from both eyes.
        ''' 
        
        if average:
            self.configure_filter(filter_type=1, filter_action=1)
        else:
            self.configure_filter(filter_type=0, filter_action=1)
                                            
    

