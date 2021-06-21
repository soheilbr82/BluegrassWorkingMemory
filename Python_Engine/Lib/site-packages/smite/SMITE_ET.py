#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Load required packages 
from psychopy import core, event, visual
from iViewXAPI import*
from iViewXAPIReturnCodes import* 
import numpy as np
import datetime
from collections import deque
from scipy import misc
import calibration_graphics as graphics
import helpers
from ctypes import *
import SMITE_raw


global buf
      
class Connect(object):
    """ Create a class that simplifies life for people wanting to use the SDK
    """
    def __init__(self, in_arg):
        '''
        Args:
            in_arg: either
                (a) string with eye tracker name, e.g., 'HiSpeed'
                (b) or settings, where 
                    settings = SMITE.get_defaults(eye_tracker_name) 

        '''
              
        # A list to store validation results
        self.calibration_history = []
        
        self.clock = core.Clock()
        
        # Connect to a class to use 'raw' SMI functionality
        rawSMI = SMITE_raw.Connect(in_arg)
        self.rawSMI = rawSMI
        self.constants = rawSMI.constants
        self.eye_tracker_name = rawSMI.eye_tracker_name
        
    #%%
    def get_options(self):
        ''' Returns current/active settings
        '''
        return self.constants           
    #%%% 
    def set_options(self):
        ''' Change current/active settings
        '''        
        pass
         
    
    #%%  
    def init(self):
        ''' Connect to the SMI eye tracker and initialize it according to 
        the requested settings
        '''
        self.rawSMI.init()        
        self.geom = self.rawSMI.get_current_RED_geometry()
        self.system_info = self.rawSMI.get_system_info()
       
    #%%    
    def is_connected(self):
        ''' Report status of the connection to the eye tracker
        
        Returns:
            rawSMI.is_connected() (boolean)
        '''
        
        return self.rawSMI.is_connected()
    
    #%% Init calibration
    def calibrate(self, win):
        ''' Do participant setup and calibration, and validation
        
        Args: 
            win - a PsychoPy window
        '''
        
        self.screen_res = win.size
        self.screen_refresh_rate = win.getActualFrameRate()
        self.mouse = event.Mouse()
        
        # Scale or shift grid or calibration points?
        # Do only if shift or scaling required in the settings file
        if np.any([self.constants.shift_cal_grid_x, 
                   self.constants.shift_cal_grid_y]) or self.scale_cal_grid != 1:
    
            # Reset calibration point to default values
            self.rawSMI.reset_calibration_points()
            
            # Get positions of current calibration points
            cal_pos = []
            for p in np.arange(self.constants.n_cal_points) + 1:
                cal_point_info = self.rawSMI.get_calibration_point(p)
                
                
                cal_pos.append([cal_point_info.positionX, 
                                cal_point_info.positionY])
    
            # Normalize point to -0.5->0.5 so they can be scaled
            cal_pos = np.array(cal_pos)
            cal_pos[:, 0] = cal_pos[:, 0] / self.screen_res[0] - 0.5
            cal_pos[:, 1] = cal_pos[:, 1] / self.screen_res[1] - 0.5
            
            # Scale 
            cal_pos[:, 0] = cal_pos[:, 0] * self.constants.scale_cal_grid
            cal_pos[:, 1] = cal_pos[:, 1] * self.constants.scale_cal_grid
            
            # Rescale to pixels
            cal_pos[:, 0] = (cal_pos[:, 0] + 0.5) * self.screen_res[0]
            cal_pos[:, 1] = (cal_pos[:, 1] + 0.5) * self.screen_res[1]
            
            # ... and shift
            cal_pos[:, 0] = cal_pos[:, 0] + self.constants.shift_cal_grid_x
            cal_pos[:, 1] = cal_pos[:, 1] + self.constants.shift_cal_grid_y            
            
            # Change to new positions
            for p in np.arange(self.constants.n_cal_points):
                self.rawSMI.change_calibration_point(p + 1, 
                                                     cal_pos[p, 0],
                                                     cal_pos[p, 1])

        # Make the window available for all calibration functions
        self.win = win        
        
        # Create click buttons used during calibration
        self._create_calibration_buttons(win)
        
        # Animated calibration?
        if self.constants.animate_calibration:
            
            # Define your calibration target
            target = helpers.MyDot(self.win, units='pix',
                                     outer_diameter = win.size[0] * 0.02, 
                                     inner_diameter = win.size[0] * 0.005)
            self.animator = AnimatedCalibrationDisplay(self.win, target, 'animate_point')
        
        # Main control loop
        action = 'setup'
        deviations = [] # List to store validation accuracies
        while True:
            
            if 'setup' in action:
                action = self._check_head_position()
            elif 'cal' in action:                                              
                success, deviations = self._run_calibration(deviations)
                if success:
                    action, selected_calibration = self._show_validation_screen(deviations)
                else:
                    action = 'setup'
            elif 'adv' in action:
                action = self._advanced_setup()
            elif 'done'in action:
                print('calibration completed')
                break
            elif 'quit' in action:
                self.win.close()
                core.quit()
                
            core.wait(0.1)
            
        # Save all calibrations (appending 1 means that the calibration was used)
        for i, devs in enumerate(deviations):
            if i == selected_calibration-1:
                self.calibration_history.append(devs + ['used'])
                
                # Write the calibration results to the idf file
                self.start_recording()
                self.send_message("Calibration results in degrees (LX, LY, RX, RY): {}".format([d for d in devs]))
                self.stop_recording()
                
            else:
                self.calibration_history.append(devs + ['not used'])  
              
    #%%  
    def start_recording(self, clear_buffer=False):
        ''' Start recording eye-movement data to idf file
        
        Args:
            clear_buffer - clear IDF buffer (removes all data)
        '''
        
        if clear_buffer:
            self.rawSMI.clear_recording_buffer()
            
        self.rawSMI.start_recording()
        
    #%% 
    def start_buffer(self, sample_buffer_length=3):
        '''Start recording eye-movement data into buffer for online use
        
        Args:
            sample_buffer_length - size of buffer in samples
        '''
        
        self.rawSMI.start_buffer(sample_buffer_length=sample_buffer_length)
        
    #%% 
    def send_message(self, msg):
        ''' Insert message into idf file
        
        Args: 
            msg - message string to put into buffer
        '''
        
        self.rawSMI.send_image_message(msg)
        
    #%%
    def get_latest_sample(self):
        ''' Get most recent data sample
        
        Returns:
            sample 
            
            Ex: sample.leftEye.gazeY
            See SMI manual for full description of what sample contains
        '''
        sample  = self.rawSMI.get_latest_sample()
        return sample
        
    #%%
    def consume_buffer_data(self):
        ''' Get data from the online buffer. The returned samples are removed 
        from the buffer
        
        Returns:
            data - list of samples (see get_latest_sample)
        '''
        data = self.rawSMI.consume_buffer_data()
        return data
    
    #%%
    def peek_buffer_data(self):
        ''' Get data from the online buffer. The returned samples remain in 
        the buffer
        
        Returns:
            data - list of samples (see get_latest_sample)        
        '''
        data = self.rawSMI.peek_buffer_data()
        return data    
    
    #%% 
    def stop_buffer(self, clear_buffer=False):
        ''' Stop recording data into buffer
        '''
        self.rawSMI.start_buffer()    
        
    #%%  
    def stop_recording(self):
        ''' Stop recording data into idf file 
        '''
        self.rawSMI.stop_recording()
        
        
    #%% 
    def save_data(self, filename, description = "", 
                   user = None, append_version=True):
        ''' Save idf file to specified location
        The data recording needs to be stopped using iV_StopRecording
        before the data buffer can be saved to given location. 
        The filename can include the path. If the connected eye tracking device 
        is an HED, scene video buffer is written, too. iV_SaveData will not return
        until the data has been saved.
        
        Args:
            filename - full path including the filename of the data file being created
            description - Optional experiment description tag stored in the idf file. This tag is available in BeGaze and in the text export from an idf file.
            user - Optional name of test person. This tag is available in BeGaze and in the text export
                    from an idf file.
            append_version - append version number to file if exists.            
                If True, and there is already a file with a certain name 'name.idf', this file will not 
                be overwritten, but save as another file with name 'name_1.idf'.            
        
        '''
        self.rawSMI.save_data(filename, description = description, 
                   user = user, append_version=append_version)        
    #%%
    def de_init(self):
        ''' Close connection to the eye tracker and clean up
        '''
        self.rawSMI.de_init()
        
    #%%
    def set_begaze_trial_image(self, imname):
        ''' Put specially prepared message in idf file to notify BeGaze what 
        stimulus image/video belongs to a trial
        
        Args:
            imname - filename of stimulus that is shown on this trial. 
            Must have one of the following extentions: .png, .jpg, .jpeg, .bmp, 
            or .avi
        '''
        
        self.rawSMI.set_begaze_trial_image(imname)
    #%%        
    def set_begaze_key_press(self, msg):
        ''' Put specially prepared message in idf file that shows up as 
        keypress in BeGaze
        
        Args: 
            msg - string that will show up on BeGaze's event timeline. 
            Can be name of a key, but also other arbitrary string.
        '''
        self.rawSMI.set_begaze_key_press(msg)
    #%%
    def set_begaze_mouse_click(self, which, x, y):
        ''' Put specially prepared message in idf file that shows up as mouse 
        click in BeGaze.
        
        Args:
            which: string indicating which mouse button, left or right
            x: horizontal coordinate of mouse click
            y: vertical coordinate of mouse click
        '''
        self.rawSMI.set_begaze_mouse_click(which, x, y)
        
    #%%
    def start_eye_image_recording(self, image_name, path):
        ''' Start recording eye images to file. Not supported on RED250mobile, 
        REDn Scientific, and REDn Professional.
        
        Args:
            image_name - filename where recorded eye images will be saved
            path - path where the eye images are stored
            
        Example: start_eye_image_recording('test',"c:\\eyeimages\\" )
        '''
        self.rawSMI.start_eye_image_recording(image_name, path)
    #%%
    def stop_eye_image_recording(self, image_name, path):
        ''' Stop recording eye images to file 
        '''
        self.rawSMI.start_eye_image_recording(image_name, path)        
        
    #%% 
    def set_dummy_mode(self):
        ''' Enable dummy mode, which allows running the program without an 
        eye tracker connected
        '''
        import SMITE_Dummy, SMITE_Dummy_raw
        self.__class__ = SMITE_Dummy.Connect
        self.__class__.__init__(self)    
        self.rawSMI = SMITE_Dummy_raw.Connect()

    #%% 
    def _create_calibration_buttons(self, win):
        '''Creates click buttons that are used during calibration
        
        Args: 
            win - PsychoPy window
        '''
        
        # Find out ratio aspect of (16:10) or 
        screen_res = win.size
        ratio = screen_res[0] / float(screen_res[1])
        
        # Shown during setup to check gaze in corners
        self.POS_CAL_CHECK_DOTS = [[-0.45 * ratio, -0.45], [0.45 * ratio, -0.45], 
                              [-0.45 * ratio, 0.45], [0.45 * ratio, 0.45]]

        # Text object to draw text (on buttons)
        #text_size = 0.04
        instruction_text = visual.TextStim(win,text='',wrapWidth = 1,height = graphics.TEXT_SIZE, units='norm')  
        self.instruction_text = instruction_text
        
        # Setup stimuli for drawing calibration / validation targets
        self.cal_dot = helpers.MyDot2(win, units='pix',
                                     outer_diameter=graphics.TARGET_SIZE, 
                                     inner_diameter=graphics.TARGET_SIZE_INNER)
        
        # Click buttons
        self.calibrate_button = visual.Rect(win, width= graphics.WIDTH_CAL_BUTTON, 
                                            height=graphics.HEIGHT_CAL_BUTTON,  
                                        units='norm', fillColor=graphics.COLOR_CAL_BUTTON,
                                        pos=graphics.POS_CAL_BUTTON)                
        self.calibrate_button_text = visual.TextStim(win, text=graphics.CAL_BUTTON_TEXT, 
                                                     height=graphics.TEXT_SIZE, units='norm',
                                                     pos=graphics.POS_CAL_BUTTON)
                                                     
        self.recalibrate_button = visual.Rect(win, width= graphics.WIDTH_RECAL_BUTTON, 
                                            height=graphics.HEIGHT_RECAL_BUTTON,  
                                        units='norm', fillColor=graphics.COLOR_RECAL_BUTTON,
                                        pos=graphics.POS_RECAL_BUTTON) 
        self.recalibrate_button_text = visual.TextStim(win, text=graphics.RECAL_BUTTON_TEXT, 
                                                     height=graphics.TEXT_SIZE, units='norm',
                                                     pos=graphics.POS_RECAL_BUTTON)                                                     
                                        
        self.setup_button = visual.Rect(win, width= graphics.WIDTH_SETUP_BUTTON, 
                                        height=graphics.HEIGHT_SETUP_BUTTON,  
                                        units='norm', fillColor=graphics.COLOR_SETUP_BUTTON,
                                        pos=graphics.POS_SETUP_BUTTON)
        self.setup_button_text = visual.TextStim(win, text=graphics.SETUP_BUTTON_TEXT, 
                                                 height=graphics.TEXT_SIZE, units='norm',
                                                 pos=graphics.POS_SETUP_BUTTON)             

        self.accept_button = visual.Rect(win, width= graphics.WIDTH_ACCEPT_BUTTON, 
                                        height=graphics.HEIGHT_ACCEPT_BUTTON,  
                                        units='norm', fillColor=graphics.COLOR_ACCEPT_BUTTON,
                                        pos=graphics.POS_ACCEPT_BUTTON)
        self.accept_button_text = visual.TextStim(win, text=graphics.ACCEPT_BUTTON_TEXT, 
                                                  height=graphics.TEXT_SIZE, units='norm',
                                                  pos=graphics.POS_ACCEPT_BUTTON)             
                                                                        
        self.back_button = visual.Rect(win, width= graphics.WIDTH_BACK_BUTTON, 
                                        height=graphics.HEIGHT_BACK_BUTTON,  
                                        units='norm', fillColor=graphics.COLOR_BACK_BUTTON,
                                        pos=graphics.POS_BACK_BUTTON)    
        self.back_button_text = visual.TextStim(win, text=graphics.BACK_BUTTON_TEXT, 
                                                height=graphics.TEXT_SIZE, units='norm',
                                                pos=graphics.POS_BACK_BUTTON)             
                                                                      
        self.gaze_button = visual.Rect(win, width= graphics.WIDTH_GAZE_BUTTON, 
                                        height=graphics.HEIGHT_GAZE_BUTTON,  
                                        units='norm', fillColor=graphics.COLOR_GAZE_BUTTON,
                                        pos=graphics.POS_GAZE_BUTTON)   
        self.gaze_button_text = visual.TextStim(win, text=graphics.GAZE_BUTTON_TEXT, 
                                                height=graphics.TEXT_SIZE, units='norm',
                                                pos=graphics.POS_GAZE_BUTTON)             
                                        
        # Dots for the setup screen
        self.setup_dot = helpers.MyDot(win, units='height',
                                     outer_diameter=graphics.SETUP_DOT_OUTER_DIAMETER, 
                                     inner_diameter=graphics.SETUP_DOT_INNER_DIAMETER)        
        
        # Setup control circles for head position
        self.static_circ = visual.Circle(win, radius = graphics.HEAD_POS_CIRCLE_FIXED_RADIUS, 
                                         lineColor = graphics.HEAD_POS_CIRCLE_FIXED_COLOR,
                                         lineWidth=4, units='height')
        self.moving_circ = visual.Circle(win, radius = graphics.HEAD_POS_CIRCLE_MOVING_RADIUS, 
                                         lineColor = graphics.HEAD_POS_CIRCLE_MOVING_COLOR,
                                         lineWidth=4, units='height')        
                                         
        # Dot for showing et data
        self.et_sample_l = visual.Circle(win, radius = graphics.ET_SAMPLE_RADIUS, 
                                         fillColor = 'blue', units='pix') 
        self.et_sample_r = visual.Circle(win, radius = graphics.ET_SAMPLE_RADIUS, 
                                         fillColor = 'red', units='pix')                                         
      
        # Show images (eye image, validation resutls)
        self.eye_image_stim = visual.GratingStim(win, units='pix', size=graphics.EYE_IMAGE_SIZE,
                                                    tex=np.zeros(graphics.EYE_IMAGE_SIZE))
        
        # Accuracy image 
        self.accuracy_image = visual.ImageStim(win, image=None,units='norm', size=(1.5,1.5),
                                          pos=(0, 0))
        
        # Tracking monitor image
        self.tracking_monitor = visual.ImageStim(win, image=None,units='norm', size=(0.5,0.5),
                                          pos=(0, -0.5), ori = 180)
        

                        
    #%%      
    def _check_head_position(self):
        ''' Check to make sure that the head is in the center of the track box
        Two circles are shown; one static (representing the center of the headbox)
        and one variable representing the head position. The head is in the center 
        of the trackbox the circles overlap.
        
        Four dot are shown in the corners. Ask the participants to fixate them
        to make sure there are not problems in the corners of the screen
        '''
        xyz_pos_eye_l = (0, 0, 0)
        xyz_pos_eye_r = (0, 0, 0)
        
        while True:
            
            # Draw four dots in the corners
            for i in self.POS_CAL_CHECK_DOTS:
                self.setup_dot.setPos(i)
                self.setup_dot.draw()

            # Draw buttons, one to calibrate, and one to 
            # go to the advanced setup screen
            self.calibrate_button.draw()
            self.calibrate_button_text.draw()   
            
            k = event.getKeys()
                
            # Plot distance information only for remotes (not HiSpeed)
            if 'RED' in self.eye_tracker_name:
                self.setup_button.draw()
                self.setup_button_text.draw()            
                
                if graphics.SETUP_BUTTON in k or self.mouse.isPressedIn(self.setup_button, buttons=[0]):
                    # Go to advanced setup screen
                    action = 'adv'
                    break     
                                 
                # Get information about where the head is in the head box
                # and visualize it
                headbox_data = self.rawSMI.get_headbox_coordinates()

                # Get position of eye in track box (average of both eyes)
                xyz_pos_eye_l = (headbox_data.leftEye.relativePositionX,
                                 headbox_data.leftEye.relativePositionY,
                                 headbox_data.leftEye.relativePositionZ)
                xyz_pos_eye_r = (headbox_data.rightEye.relativePositionX,
                                 headbox_data.rightEye.relativePositionY,
                                 headbox_data.rightEye.relativePositionZ)
              
                # Get the average head position
                avg_pos = []
                for i in np.arange(len(xyz_pos_eye_r)):
                    avg_pos.append((xyz_pos_eye_l[i] + xyz_pos_eye_r[i]) / 2.0)   
                    
                # Draw moving circle based on the data (0.5, 0.5, 0.5)  means the 
                # eye is in the center of the box
                self.moving_circ.pos = avg_pos[0], avg_pos[1]
                self.moving_circ.radius = avg_pos[2] * 0.30 + graphics.HEAD_POS_CIRCLE_FIXED_RADIUS
    
                # Restrict min and max size of circles
                if self.moving_circ.radius < 0.01:
                    self.moving_circ.radius = 0.01
                    
                if self.moving_circ.radius > 0.3:
                    self.moving_circ.radius = 0.3
    
                # Draw circles
                self.moving_circ.draw()
                self.static_circ.draw()
                            
                # Draw instruction
                self.instruction_text.pos = (0, 0.8)
                self.instruction_text.text = 'Position yourself such that the two circles overlap.'
                self.instruction_text.draw()
                
                # Get and draw distance information
                sample_data = self.rawSMI.get_latest_sample()
                l_pos = sample_data.leftEye.eyePositionZ
                r_pos = sample_data.rightEye.eyePositionZ
                
                try:
                    self.instruction_text.pos = (0, 0.7)
                    self.instruction_text.text = ' '.join(['Distance:', str(int((l_pos + r_pos)/2.0/10)), 'cm'])
                    self.instruction_text.draw() 
                except:
                    pass
            else:
                # 'Hidden' button in the HiSpeed mode
                if graphics.SETUP_BUTTON in k:
                    action = 'adv'
                    break 
                    
            # check whether someone left clicked any of the buttons or pressed 'space'
            if graphics.CAL_BUTTON in k or self.mouse.isPressedIn(self.calibrate_button, buttons=[0]):
                action = 'cal'
                break
                
            if 'escape' in k:
                action = 'quit'
                break
                    
            # Option to skip calibration (no button for this?)
            if 'return' in k:
                action = 'done'
                break               
            
            # Update the screen
            self.win.flip()
         
        return action
        
    #%%        
    def _run_calibration(self, deviations, show_instructions=False,
                   select_best_calibration=False, optional=False):
        """ Run the calibration
        
        Args: 
            deviations - list containing results from previous calibrations
            show_instruction - show calibration instructions 
            select_best_calibration - option to store and select from all performed
                                        calibrations
            optional - is the calibration optional or required (allows you to 
                       skip the calibration if set to True).
        """
                
        self.win.flip()
        self.instruction_text.pos = (0, 0)
        self.instruction_text.color = (-1, -1, -1)
        
        print('calibration started')
        
        # Optional calibration
        if optional:
            self.instruction_text.setText('Press q to calibrate or any other key to continue')
            self.instruction_text.draw()
            self.win.flip()
            k = event.waitKeys()
            if not 'q' in k[0]:   
                return False, deviations
                
        # Show calibration instructions
        if show_instructions:
            self.instruction_text.setText(
                'A number of dots will be presented on the screen. Carefully look in the center of each dot for as long as it is shown.\n '
                '(press space to begin).')
            self.instruction_text.draw()
            self.win.flip()
            event.waitKeys()
                  
        print('calibration_start')
        
        validation_successful = False
        while not validation_successful:
            # Calibrate using PsychoPy (dots are drawn by PsychoPy)
            calibration_state = self._calibrate_custom(mode = 'cal')
            
            # if the calibration is successful, start a validation
            if calibration_state == 1:
                calibration_state = self._calibrate_custom(mode = 'val')
                if calibration_state == 1:
                    validation_successful = True
               
            # if the calibration failed (someone pressed escape, return unsuccessful calibration)
            if calibration_state == 2:
                break
                
        # Get accuracy values (only if validation success)
        if validation_successful:
            accuracy = self.rawSMI.get_accuracy()
            print('calibration_end')
            
            # Save calibration Display accuracy values
            now = datetime.datetime.now() # Get current time
            deviations.append([str(accuracy[0])[:4],
                               str(accuracy[1])[:4],
                               str(accuracy[2])[:4],
                               str(accuracy[3])[:4],
                               now.isoformat()])
            
        return validation_successful, deviations
    #%%     
    def _advanced_setup(self):
        ''' Shows eye image and tracking monitor
        Good if you are having problems in the circle setup, 
        and want to see what is wrong.
        
        '''
        print('advanced mode')
        
        # Keep track of whether overlays are displayed
        toggle_state_pupil = False
        toggle_state_cr = False
   
        action = 'setup'
        
        # Create toggle buttons for pupil and CR crosshairs
        toggle_buttons = []
        n_toggle_Buttons = 2 # pupil, CR
        
        button_pos = ((0.5, 0), (0.5, -0.1))
        button_text = ['pupil (p)', 'CR (c)']
        for i in range(n_toggle_Buttons):
            toggle_buttons.append(visual.Rect(self.win, width= 0.15, 
                                                height= 0.06, 
                                                units='norm',
                                                fillColor=graphics.blue,
                                                pos=button_pos[i]))
        
        dist = 0
        done = False

        while not done:
            
            if 'HiSpeed' not in self.eye_tracker_name:
                
                # Get eye tracker distance 
                sample_data = self.get_latest_sample()
                dist = (sample_data.leftEye.eyePositionZ + 
                        sample_data.rightEye.eyePositionZ) / 2.0
                
                # Draw instruction
                self.instruction_text.pos = (0, 0.7)
                self.instruction_text.text = ' '.join(['Distance:', str(dist / 10.0)[:2], 'cm'])
                self.instruction_text.draw()
                                       
                # Draw buttons
                self.back_button.draw()
                self.back_button_text.draw()
            
            # Draw calibration button for all systems
            self.calibrate_button.draw()
            self.calibrate_button_text.draw()
            
            # Draw four dots in the corners
            for i in self.POS_CAL_CHECK_DOTS:
                self.setup_dot.setPos(i)
                self.setup_dot.draw()               
            
            # Check for keypress or mouse click to toggle visibility of pupil and CR corsshairs
            # of move on with setup
            k = event.getKeys()
            
            # The option to toggle pupil and CR buttons is only available in the REDm
            if self.eye_tracker_name == 'REDm':
                
                # Draw toggle buttons and text
                for i in range(n_toggle_Buttons):
                    toggle_buttons[i].draw()
                    self.instruction_text.text = button_text[i]
                    self.instruction_text.pos = button_pos[i]
                    self.instruction_text.draw()
                
                # Check if mouse is clicked on a toggle button
                button_clicked = -1
                for i, button in enumerate(toggle_buttons):
                    if self.mouse.isPressedIn(button):
                        button_clicked = i
                
                # Check whether keys or mouse are pressed/clicked
                if 'p' in k or button_clicked == 0:
                    if self.clock.getTime() > 1:
                        if toggle_state_pupil:
                            activate = 0
                            toggle_buttons[0].fillColor = graphics.blue
                        else:
                            activate = 1
                            toggle_buttons[0].fillColor = graphics.blue_active
                        
                        toggle_state_pupil = not toggle_state_pupil                    
                        res = self.rawSMI.set_tracking_parameter(eye_type=2,
                                                           parameter_type=4,
                                                           activate=activate)
                        self.clock.reset()
    
                elif 'c' in k or button_clicked == 1:  
                    if self.clock.getTime() > 1:
                        if toggle_state_cr:
                            activate = 0
                            toggle_buttons[1].fillColor = graphics.blue
                        else:
                            activate = 1
                            toggle_buttons[1].fillColor = graphics.blue_active
                        
                        toggle_state_cr = not toggle_state_cr                    
                        res = self.rawSMI.set_tracking_parameter(eye_type=2, 
                                                           parameter_type=5, 
                                                           activate=activate)
                                                           
                        self.clock.reset()
            
            # Draw eye image
            eye_image, res = self.rawSMI.get_eye_image()
            if res == 1:
                self.eye_image_stim.tex = eye_image

            self.eye_image_stim.draw()
              
            # Show tracking monitor (not available for HiSpeed)
            if 'HiSpeed' not in self.eye_tracker_name: 
                tracking_monitor_image, res = self.rawSMI.get_tracking_monitor()
                if res == 1:
                    self.tracking_monitor.image = tracking_monitor_image
                self.tracking_monitor.draw()
                
                # Check keypress and mouse clicks
                if graphics.BACK_BUTTON in k or self.mouse.isPressedIn(self.back_button, buttons=[0]):
                    action = 'setup'
                    break
                
            # Check keypress and mouse clicks
            if graphics.CAL_BUTTON in k or self.mouse.isPressedIn(self.calibrate_button, buttons=[0]):
                action = 'cal'
                break

                
            self.win.flip()

        return action
    #%%     
    def _show_validation_screen(self, deviations):
        ''' Shows validation image after a validation has been completed.
        The validation screen includes both visual and numerical feedback 
        about the calibration.
        '''    
        
        # Center position of presented calibration values
        x_pos_res = 0.4
        y_pos_res = 0
        
        # get (and save) validation screen image
        nCalibrations = len(deviations)
        fname = str(nCalibrations)+'.jpg'
        im = self.rawSMI.get_accuracy_image(fname) 
        
        # Save calibration 
        self.rawSMI.save_calibration(str(nCalibrations))
        core.wait(0.2)
        
        # Add image as texture
        self.accuracy_image.image = fname
        
        # information about data quality header
        header = ['Accuracy', 'LX', 'LY', 'RX', 'RY']
        x_pos= np.linspace(-0.20, 0.20, num = 5)     
        
        # Prepare header
        header_text = []    
        for j, x in enumerate(x_pos):
            header_text.append(visual.TextStim(self.win,text=header[j],
                                                wrapWidth = 1,
                                                height = graphics.TEXT_SIZE, 
                                                units='norm',
                                                pos = (x, 0.1),
                                                color = (1, 1, 1)))        
        
        # Prepare rects for buttons, button text, and accuracy values
        select_accuracy_rect = []
        select_rect_text = []
        accuracy_values = []

        y_pos = y_pos_res
        #print(self.deviations)
        for i in range(nCalibrations):
            #print(self.deviations[i])
            select_accuracy_rect.append(visual.Rect(self.win, width= 0.15, 
                                                height= 0.05, 
                                                units='norm',
                                                pos = (x_pos_res, y_pos)))
                                                
            select_rect_text.append(visual.TextStim(self.win,
                                                    text='Select',
                                                    wrapWidth = 1,
                                                    height = graphics.TEXT_SIZE, 
                                                    units='norm',
                                                    pos = (x_pos_res, y_pos)))  
                    
            # Then prepare the accuracy values for each calibration preceded 
            # by Cal x (the calibration number)
            accuracy_values_j = []
            for j, x in enumerate(x_pos):       
                #print(deviations)
                if j > 0:
                    accuracy_values_j.append(visual.TextStim(self.win,
                                                        text='{0:.2f}'.format(float(deviations[i][j - 1])),
                                                        wrapWidth = 1,
                                                        height = graphics.TEXT_SIZE, 
                                                        units='norm',
                                                        pos = (x, y_pos),
                                                        color = (1, 1, 1)))                
                else:
                    accuracy_values_j.append(visual.TextStim(self.win,
                                                        text='Cal' + str(i+1) + ':',
                                                        wrapWidth = 1,
                                                        height = graphics.TEXT_SIZE, 
                                                        units='norm',
                                                        pos = (x, y_pos),
                                                        color = (1, 1, 1))) 
            accuracy_values.append(accuracy_values_j)                 
            y_pos -= 0.06
        
        # Wait for user input
        selected_calibration = nCalibrations # keep track of which calibration is selected
        selection_done = False
        display_gaze = False
        gaze_button_pressed = False
        while not selection_done:
                        
            # Draw validation results image
            self.accuracy_image.draw()
                                   
            # Draw buttons (re-calibrate, accept and move on, show gaze)
            self.recalibrate_button.draw()
            self.recalibrate_button_text.draw()
            
            self.accept_button.draw()
            self.accept_button_text.draw()
            
            self.gaze_button.draw()
            self.gaze_button_text.draw()            
                        
            # Now draw accuracy values
            if self.constants.select_best_calibration:
                    
                # Print a list of deviations from all calibrations and choose one to continue
                # ToDo (mark selected text)
                ins = ''
               
                # Draw header
                [h.draw() for h in header_text]
                    
                # Draw accuracy values and define rectangles to select a calibration
                y_pos = 0
                
                for i in range(nCalibrations):
                    
                   # Highlight selected calibrations
                    if i == selected_calibration - 1: # Calibration selected
                        select_accuracy_rect[i].fillColor = graphics.blue_active
                        if nCalibrations > 1:
                            select_accuracy_rect[i].draw() 
                            select_rect_text[i].draw()     
                    else:
    #                    select_rect_text[i].color = graphics.blue
                        select_accuracy_rect[i].fillColor = graphics.blue
                        select_accuracy_rect[i].draw() 
                        select_rect_text[i].draw()  
                    
                    # Then draw the accuracy values for each calibration preceded 
                    # by Cal x (the calibration number)                    
                    for j, x in enumerate(x_pos): 
                        accuracy_values[i][j].draw()          
                        
                        
                    y_pos -= 0.06
                        
            else:        
                ins = deviations[-1]
                        
            # Check if mouse is clicked to select a calibration
            for i, button in enumerate(select_accuracy_rect):
                if self.mouse.isPressedIn(button):
                    self.rawSMI.load_calibration(str(i + 1))  # Load the selected calibration
                    fname = str(i + 1) + '.jpg'
                    self.accuracy_image.image = fname
                    selected_calibration = int(i + 1)
                    break
                    
            
            # Check if key or button is pressed
            k = event.getKeys()
            if graphics.RECAL_BUTTON in k or self.mouse.isPressedIn(self.recalibrate_button):
                action = 'setup'
                selection_done = True
            elif graphics.ACCEPT_BUTTON in k or self.mouse.isPressedIn(self.accept_button):
                action = 'done'
                selection_done = True                
            elif k:
                if k[0].isdigit():
                    if any([s for s in range(nCalibrations+1) if s == int(k[0])]):
                        self.rawSMI.load_calibration(k[0])  # Load the selected calibration
                        fname = str(k[0]) + '.jpg'
                        self.accuracy_image.image = fname
                        selected_calibration = int(k[0])       
                        
            elif 'escape' in k:
                action = 'quit'
                break
                
            # Toggle display gaze
            if graphics.GAZE_BUTTON in k or (self.mouse.isPressedIn(self.gaze_button, buttons=[0]) and not gaze_button_pressed):
                display_gaze = not display_gaze
                gaze_button_pressed = True
                
            # Check whether mouse button released
            if not np.any(self.mouse.getPressed()):
                gaze_button_pressed = False
              
            # Display gaze along with four dots in the corners
            if display_gaze:
                for i in self.POS_CAL_CHECK_DOTS:
                    self.setup_dot.setPos(i)
                    self.setup_dot.draw()
                self._draw_gaze(self.win.size)
        
            self.win.flip() 

        # Clear screen and return
        self.instruction_text.color = (1, 1, 1)
        self.win.flip()
        
        return action, selected_calibration
    

    #%%             
    def _calibrate_custom(self, mode = 'cal'):
        '''
        Draw own calibration dots in PsychoPy instead of using visualizations by SMI
        Used for both valication and calibration. 
        
        Args:
            mode - calibrate ('cal') or validate ('val')
        '''
        
        # If in validation mode, and semiautomatic mode is used, skip manual accept of first point
        temp_autoaccept = self.constants.autoaccept
        if 'val' in  mode and self.constants.autoaccept == 1:
            temp_autoaccept = 2
            self.rawSMI.setup_calibration_parameters(autoaccept=temp_autoaccept,
                                          cal_method=self.constants.n_cal_points, 
                                          cal_speed=self.constants.cal_speed,
                                          screen = self.constants.screen)
            
        if 'cal' in mode:
            self.rawSMI.calibrate_iview()
        else:
            self.rawSMI.validate_iview()
        
        # Record data during calibration and validation?
        if self.constants.record_data_during_calibration:
            self.start_recording()
            now = datetime.datetime.now()
            self.send_message(mode + 'started: ' + now.isoformat())
        
        calibration_done = False 
        calibration_state = 1 # 0 - calibration should be restarted
                              # 1 - calibration/validation succeded
                              # 2 - calibration/validation should be interrupted. Return to setup screen
        
        p_old = -1
        p = -1
        tick = 0
        pos_old = (0, 0)
        x_old, y_old = 0, 0
        animation_state = 'static' # or move
        while not calibration_done:
                     
            # Update currentCalibrationPoint struct
            res, currentCalibrationPoint = self.rawSMI.get_current_calibration_point()
            
            # Draw and show calibration point 
            if res == 1:
                
                # Get information about current calibration point and draw it
                p = currentCalibrationPoint.number
                x = currentCalibrationPoint.positionX
                y = currentCalibrationPoint.positionY
                
                # if the calibration point has changed
                if p != p_old:
                    
                    # Write information about dot position to idf file
                    if self.constants.record_data_during_calibration:              
                        now = datetime.datetime.now()
                        self.send_message('_'.join([mode, str(p), str(x), str(y), now.isoformat()]))
                    p_old = p
                    pos_old = (x_old, y_old)
                    tick = 0
                    animation_state = 'move'                         
               
                # Convert to psychopy coordinates
                xy = helpers.smi2psychopy(np.array([[x, y]]), self.win.monitor, units='pix')
                
                # Animate calibration dots or show static dots?
                if self.constants.animate_calibration:
                    if animation_state == 'move':                    
                        move_completed = self.animator.move_point(pos_old, (xy[:, 0], xy[:, 1]), tick)
                        if move_completed:
                            animation_state = 'static' # or move
                            tick = 0
                    else:
                        self.animator.animate_target(p, (xy[:, 0], xy[:, 1]), tick)
                else:
                    self.cal_dot.setPos(xy)
                    self.cal_dot.draw()
                
                self.win.flip()
                    
                x_old = xy[:, 0]
                y_old = xy[:, 1]
                
            # if no new data available, quit calibration.
            elif res == 2:
                calibration_done = True
            else: # If other messages occur, ignore them (sometimes complaints of connection loss)
                pass
                
            # Accept calibration point
            k = event.getKeys()      
            if temp_autoaccept == 2: # Automatic accept
                pass
            elif temp_autoaccept == 0: # Manual accept
                if 'space' in k and self.clock.getTime() > 0.5:
                    self.rawSMI.accept_calibration_point()
                    self.clock.reset()
            else: # if first point, wait for keypress, otherwise continue automatically
                if p == 1: 
                    if 'space' in k:
                        self.rawSMI.accept_calibration_point()
             
            # Abort calibration if esc is pressed (and go back to setup screen)
            if 'escape' in k:
                self.rawSMI.abort_calibration()
                calibration_state = 2
                break
                
            # 'r' aborts and restarts calibration 
            if 'r' in k:
                tick = 0
                self.rawSMI.abort_calibration()                          
                calibration_state = 0
                break
             
            tick += 1
        
        # Stop recording (if recording)
        if self.constants.record_data_during_calibration:
            now = datetime.datetime.now()
            self.send_message(mode + 'stopped: ' + now.isoformat())                    
            self.stop_recording()
            
        self.win.flip()
        event.clearEvents()
        
        # Change back to default point acceptence mode
        if 'val' in  mode and self.constants.autoaccept == 1:
            self.rawSMI.setup_calibration_parameters(autoaccept=self.constants.autoaccept,
                                          cal_method=self.constants.n_cal_points, 
                                          cal_speed=self.constants.cal_speed,
                                          screen = self.constants.screen)            
        
        return calibration_state
        

    #%%                           
    def _show_gaze(self):
        ''' Display gaze data until a keypress
        '''
        while True:
            self._draw_gaze()
            k = event.getKeys()
            if k:
                break
                
            #core.wait(1.0 / self.screen_refresh_rate)
            self.win.flip()
    #%%             
    def _draw_gaze(self):
        '''  Draws gaze data as circles for both eyes
        '''
            
        # Get latest gaze data and draw them
        sample_data = self.get_latest_sample()
                        
        xl = sample_data.leftEye.gazeX
        yl = sample_data.leftEye.gazeY 
        xr = sample_data.rightEye.gazeX
        yr = sample_data.rightEye.gazeY
        
        pos = helpers.smi2psychopy(np.array([[xl, yl]]), self.win.monitor)
        self.et_sample_l.pos = (pos[:, 0][0], pos[:, 1][0])
        self.et_sample_l.draw()
        
        pos = helpers.smi2psychopy(np.array([[xr, yr]]), self.win.monitor)
        self.et_sample_r.pos = (pos[:, 0][0], pos[:, 1][0])
        self.et_sample_r.draw()            

#%%   
class AnimatedCalibrationDisplay(object):
    """ A class for drawing animated targets"""
    def __init__(self, win, target, function_name):
        ''' The function 'function_name' does the actual drawing
        '''
        self.win = win
        self.function_name = function_name
        self.target = target # psychopy.visual object (should be in 'pix' units)
        self.screen_refresh_rate = float(win.getActualFrameRate())
        
    def animate_target(self, point_number, position, tick):
        ''' Calls the target drawing function 'func'
        '''

        eval(''.join(['self.',self.function_name,'(',str(point_number),',', 
                                        '(',str(position[0][0]),',',
                                            str(position[1][0]), ')' ,',', str(tick),')']))
        
            
    def animate_point(self, point_number, position, tick):
        ''' Animates calibration point with a certain point_number and position
        tick increases by 1 for each call
        Args:
            position - (x, y)
        '''
        
        target_size = np.abs(1 - np.sin(3 * tick / self.screen_refresh_rate + 3*np.pi/2)) + 0.2
        self.target.setSize(target_size)
        self.target.setPos(position)
        self.target.draw()
        
    def move_point(self, old_position, new_position, tick):
        ''' Animates movement between two positions
        '''
        move_completed = False
        
        # The target should have a fixed size when moving
        self.target.setSize(2)
        
        # How many ticks should the movement be (one screen unit in one second)?
        n_steps = self.screen_refresh_rate / 2
        step_pos_x = np.linspace(old_position[0], new_position[0], n_steps)
        step_pos_y = np.linspace(old_position[1], new_position[1], n_steps)
        
        if tick >= len(step_pos_x):
            move_completed = True
        else:       
            self.target.setPos((step_pos_x[tick], step_pos_y[tick]))
            
        self.target.draw()
        
        return move_completed

        
        
        
        
    
