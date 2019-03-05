PhD Student: Soheil Borhani, sborhani at vols.utk.edu
Research Assistant: Michael O'neil, moneil8 at vols.utk.edu

#######################################################################
Zhao's Brain-computer interface lab, University of Tennessee, Knoxville
Yang's ABC lab, University of Kentucky, Lexington
Bluegrass Short-term Memory and Neurofeedback paradigm has been developed by Dr. Yang Jiang 

#######################################################################
Requirements:
1. Psychopy
2. pylsl
3. python xlrd library
4. LabRecorder
5. xdf file loader (Python and MATLAB)



Optional Requirements:
1. MATLAB Importer (for importing xdf data files in MATLAB)
2. MATLAB Viewer (for online displaying the data stream)

#######################################################################
Installation:
Prerequisite software libraries installation:
1.Install Psychopy dependencies first:
http://psychopy.org/installation.html

	a.Install Python:
	Python 3.6 is preferred. It is recommended to select “install for all Users”.


	b.Install python LSL module:

	Run this command:
	$ pip install pylsl
 
2.Install Psychopy:
Download StandalonePsychoPy3_PY2-3.0.1-win32.exe file for Windows system from the link below:
https://github.com/psychopy/psychopy/releases

#######################################################################
Instruction:
The platform is designed to evaluate Working Memory using Neurophysiological signals.
The setup can be extended to synchronously collect other types of behavioral and
physiological signals (Heart rate, saccade, GSR, etc.).
Doube-clicking on "BluegrassWM.psyexp" will run the experiment. 

#######################################################################
Bluegrass WM Markers:
'b' : The onset of each block of stimuli

'a' or 'l' : The onset of each trial 'a' for targets and 'l' for non-targets

'f': The onset of fixation

'1': Correct responses

'2': Incorrect responses

'n': The onset of Inter-trial

'e': The end of the experiment

Resting state EEG Markers:
'f': The onset of fixation

'o': The onset of eyes open

'c': The onset of eyes close

'n': The onset of Inter-trial

'e': The end of the experiment
#######################################################################
Recording File Format:
The recording program (LabRecorder) and Python/C++ library (RecorderLib) record into the XDF file 
format (Extensible Data Format, hosted at https://github.com/sccn/xdf). XDF was designed concurrently 
with the lab streaming layer and supports the full feature set of LSL (including multi-stream container 
files, per-stream arbitrarily large XML headers, all sample formats as well as time-synchronization information).