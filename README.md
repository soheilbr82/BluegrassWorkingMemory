# Bluegrass Short-term memory evaluation paradigm

This is a python-based implementation of Bluegrass short-term memory. The setup is able to synchronously collect behavioral, neural, and any other LSL-compatible neurophysiological signals.
The setup can be extended to synchronously collect other types of behavioral and physiological signals (Heart rate, saccade, GSR, etc.).

The setup is developed by:\
Soheil Borhani, sborhani@vols.utk.edu\
Michael O'neil, moneil8@vols.utk.edu

This is achieved in collaboration with:\
Zhao's Nonlinear Biodynamics lab, University of Tennessee, Knoxville\
Jiang's ABC lab, University of Kentucky, Lexington

Bluegrass Short-term Memory paradigm was originally designed by Dr. Yang Jiang.

## Installation
The setup is generally OS-independent. However, the below instruction is for Windows 10.


1. Install standalone PsychoPy. 
The setup should be compatible with the latest version of PsychoPy. You can download it from [this](https://github.com/psychopy/psychopy/releases) link. Although the setup may work properly on python 2.7, I recommend using standalone PsychoPy with python 3.



2. Install pylsl for recording labstreaminglayer (LSL) streams.
LSL is a gold-standard for synchronous neurophysiological data collection and this platform is designed in a way that supports data collection using LSL protocol. Using LSL at the core of the setup makes it universal and vendor-independent.

> You may need administrator privilege for installing the package. Assuming installation of PsychoPy in default route, you can install pylsl using this command:
```windows
C:\Program Files (x86)\PsychoPy3>python -m pip install pylsl
```



3. Install (win)pexpect for seamlessly start and stop LSL data recording.
LabRecorder collects neurophysiological signal streams in LSL seamlessly in the background. We need (win)pexpect library to call LabRecorder.


> You may need administrator privilege for installing the package. Assuming installation of PsychoPy in default route, you can install (win)pexpect using this command:
```windows
C:\Program Files (x86)\PsychoPy3>python -m pip install winpexpect
```



4. Install xlrd for reading stimuli excel file.
The setup presented a pseudo-random sequence of stimuli to the participants. The specifics of the stimuli is coded in multiple excel files. The setup requires xlrd python library to call and access to the excel files.


> You may need administrator privilege for installing the package. Assuming installation of PsychoPy in default route, you can install xlrd using this command:
```windows
C:\Program Files (x86)\PsychoPy3>python -m pip install xlrd
```



## Stream markers
'b' : The onset of each block of stimuli

'a' or 'l' : The onset of image trials 'a' for targets and 'l' for non-targets

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


## Recording File Format
LabRecorder record into the XDF file format (Extensible Data Format, hosted at https://github.com/sccn/xdf). XDF was designed concurrently with the lab streaming layer and supports the full feature set of LSL (including multi-stream container files, per-stream arbitrarily large XML headers, all sample formats as well as time-synchronization information).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Reference
If you find this platform and the associated code useful for your research, please cite:

```
@article{borhani2019connectivity,
	author = {Borhani, Soheil and Abiri, Reza and Jiang, Yang and Berger, Taylor and Zhao, Xiaopeng},
	title = {Brain connectivity evaluation during selective attention using EEG-based brain-computer interface},
	journal = {Brain-Computer Interfaces},
	volume = {0},
	number = {0},
	pages = {1-11},
	year  = {2019},
	publisher = {Taylor & Francis},
	doi = {10.1080/2326263X.2019.1651186},
	URL = {https://doi.org/10.1080/2326263X.2019.1651186},
	eprint = {https://doi.org/10.1080/2326263X.2019.1651186}
}
```