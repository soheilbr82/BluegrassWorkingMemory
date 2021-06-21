# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:19:10 2018

@author: Marcus
"""
import numpy as np

blue = tuple(np.array([37, 97, 163]) / 255.0 * 2 - 1)
blue_active = tuple(np.array([11, 122, 244]) / 255.0 * 2 - 1)
green = tuple(np.array([0, 120, 0]) / 255.0 * 2 - 1)
red = tuple(np.array([150, 0, 0]) / 255.0 * 2 - 1)
yellow = tuple(np.array([150, 150, 0]) / 255.0 * 2 - 1)

ET_SAMPLE_RADIUS = 10 # Pixles

# Size of text
TEXT_SIZE = 0.04

# SIze of calibration dots
TARGET_SIZE=20  # in pixles
TARGET_SIZE_INNER=TARGET_SIZE / float(5)  # inner diameter of dot

HEAD_POS_CIRCLE_FIXED_COLOR = blue
HEAD_POS_CIRCLE_FIXED_RADIUS = 0.15

HEAD_POS_CIRCLE_MOVING_COLOR = yellow
HEAD_POS_CIRCLE_MOVING_RADIUS = 0.15

POS_CAL_BUTTON = (0.5, -0.8)
COLOR_CAL_BUTTON =  green
WIDTH_CAL_BUTTON = 0.30
HEIGHT_CAL_BUTTON = 0.08
CAL_BUTTON = 'space'
CAL_BUTTON_TEXT = 'calibrate (spacebar)'

POS_RECAL_BUTTON = (-0.5, -0.8)
COLOR_RECAL_BUTTON =  red
WIDTH_RECAL_BUTTON = 0.30
HEIGHT_RECAL_BUTTON = 0.08
RECAL_BUTTON = 'c'
RECAL_BUTTON_TEXT = 'recalibrate (c)'

# Button for advanced setup
POS_SETUP_BUTTON = (-0.5, -0.8)
COLOR_SETUP_BUTTON = blue
WIDTH_SETUP_BUTTON = 0.30
HEIGHT_SETUP_BUTTON = 0.08
SETUP_BUTTON = 'a'
SETUP_BUTTON_TEXT = 'advanced (a)'

POS_ACCEPT_BUTTON = (0.5, -0.8)
COLOR_ACCEPT_BUTTON = green
WIDTH_ACCEPT_BUTTON = 0.30
HEIGHT_ACCEPT_BUTTON = 0.08
ACCEPT_BUTTON = 'space'
ACCEPT_BUTTON_TEXT = 'accept (spacebar)'

POS_BACK_BUTTON = (-0.5, -0.8)
COLOR_BACK_BUTTON = blue
WIDTH_BACK_BUTTON = 0.30
HEIGHT_BACK_BUTTON = 0.08
BACK_BUTTON = 'b'
BACK_BUTTON_TEXT = 'basic (b)'

POS_GAZE_BUTTON = (0.5, 0.8)
COLOR_GAZE_BUTTON = blue
WIDTH_GAZE_BUTTON = 0.25
HEIGHT_GAZE_BUTTON = 0.08
GAZE_BUTTON = 'g'
GAZE_BUTTON_TEXT = 'show gaze (g)'

SETUP_DOT_OUTER_DIAMETER = 0.05 # Height unit
SETUP_DOT_INNER_DIAMETER = 0.02        

#EYE_IMAGE_SIZE = (640, 512)
EYE_IMAGE_SIZE = (512, 512)

