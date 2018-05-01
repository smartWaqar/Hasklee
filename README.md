# Hasklee
Hasklee is a concolic testing engine for Haskell which is implemented in python.

Python Version: 2.7.13
GHC Version: 7.10.2

Program Consists of two files: 

     1. hsInstrumenter.py 
     2. hasKlee.py
     
How to run the program:

> python hsInstrumnter_v2.py inputFileName
> python hasKlee_v2.py

Note: hsInstrumenter require input filename.

The code in this directory supports funtions which supports:

    - Arbitrary level of nestedes.
    - One variable,  which by convention is named x1 in the parent function.
    

There are two other directories:
     - multivariable
     - examples
     
Multivariable directory contains the program which support multivarialbe functions.
Examples directory contains 3 example input files.
