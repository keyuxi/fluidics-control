## fluidics-control ##
This is a repository of code for controlling a series of motorized CNC well selectors, valves, and fluidics pumps for automated fluid handling. The software communicates with [storm-control](https://github.com/BoettigerLab/storm-control) to allow integration in imaging experiments. 

## Contributions ##
The original version of the controller was developed in the Zhuang Lab, primarily by Jeff Moffitt, designed for integration with the lab's storm-control software, written primarily by Hazen Babcock.

The software has been expanded to allow use of a motorized CNC well-selector, written by Nasa Sinnott-Armstrong.

## Installation ##
You will need Python and PyQt as well as a number of other libraries. 

## Directory Layout ##
fluidics - This folder contains software (kilroy.py) to control a series of pumps and valves so that fluid control can be integrated with imaging. 

sc_library - This folder contains the modules that are used in multiple different programs.


## General notes ##
1. This software is written primarily in Python with a few C helper libraries.

3. The software is provided "as is" in the hope that others might find it useful. While it is fairly stable and has been developed and used since 2009 in the Zhuang lab, we provide no guarantee that any future changes that are made will maintain backwards compatibility with older versions.

