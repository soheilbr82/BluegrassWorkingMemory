#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Load required packages 
from psychopy import core, event, misc, visual
import numpy as np
import SMITE_Dummy_raw
        
class Connect(object):
    """
    Creates a class that simplifies life for people wanting to use the SDK
    """
    def __init__(self):

        self.rawSMI = SMITE_Dummy_raw.Connect()
        
        # Mouse object
        self.mouse = event.Mouse()
        
        # clock
        self.clock = core.Clock()
     
    def init(self):
        ''' Connect to eye tracker
        and apply settings
        '''
        self.rawSMI.init()           
        self.geom = None
        self.system_info = None
        self.calibration_history = None
    #%%    
    def is_connected(self):
        self.rawSMI.is_connected()
    
    #%% Init calibration
    def calibrate(self, win):
        ''' Master function for setup and calibration
        '''
        
        # Window and instruction text for calibration        
        instruction_text = visual.TextStim(win,text='',wrapWidth = 1,
                                           height = 0.05, units='norm')  
        
        self.instruction_text = instruction_text
        
        self.win = win
        self.rawSMI.win = win
        
        self.instruction_text.text = 'Calibration Dummy mode'
        self.instruction_text.draw()
        self.win.flip()
        core.wait(2)
                
    #%%  
    def start_recording(self):
        self.rawSMI.start_recording()
        
    #%% 
    def start_buffer(self, sample_buffer_length=3):
        self.rawSMI.start_buffer(sample_buffer_length=sample_buffer_length)
        
    #%% 
    def send_message(self, msg):
        self.rawSMI.send_image_message(msg)
        
    #%%
    def get_latest_sample(self):
        sample  = self.rawSMI.get_latest_sample()
        return sample
        
    #%%
    def consume_buffer_data(self):
        data = self.rawSMI.consume_buffer_data()
        return data
    
    #%%
    def peek_buffer_data(self):
        data = self.rawSMI.peek_buffer_data()
        return data    
    
    #%% 
    def stop_buffer(self):
        self.rawSMI.start_buffer()    
        
    #%%  
    def stop_recording(self):
        self.rawSMI.stop_recording()
    #%% 
    def save_data(self, filename, description = "", 
                   user = None, overwrite=0):
        self.rawSMI.save_data(filename, description = "", 
                   user = None, overwrite=0)        
    #%%
    def de_init(self):
        self.rawSMI.de_init()
        
    #%%
    def set_begaze_trial_image(self, imname):
        self.rawSMI.set_begaze_trial_image(imname)
    #%%        
    def set_begaze_key_press(self, msg):
        self.rawSMI.set_begaze_key_press(msg)
    #%%
    def set_begaze_mouse_click(self, which, x, y):
        self.rawSMI.set_begaze_mouse_click(which, x, y)      
        
    #%%
    def start_eye_image_recording(self, image_name, path):
        self.rawSMI.start_eye_image_recording(image_name, path)
    #%%
    def stop_eye_image_recording(self, image_name, path):
        self.rawSMI.start_eye_image_recording(image_name, path)        
        
    #%% 
    def set_dummy_mode(self):
        print('Does nothing')



   
 