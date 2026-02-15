README.TXT

The program ‘PeEn-run-v-0.3.py‘ is used to evaluate entropy of a signals (in this case of ECG recordings), but it can be applied to any signal.

The evaluation principle:
********************

A signal is split into segments of predefined width (‘w’), which are evaluated by PeEn. Each segment produce one PeEn value. The segment is evaluated using ‘d’ points. Their ordering is defined and added to a distribution of orderings. Subsequently, the distribution is inserted into information entropy formula that gives the value of PeEn for the given segment.

Beware, the width ‘w’ of the segment must be sufficient to accommodate many sequences of points in order to produce a sufficient number of values in the distribution.

Running the program:
*****************

‘python3 PeEn-run-20260206.py -i ./False-ECG-sinus.csv -w 500 -d 3 -e 1’

where

‘PeEn-run-20260206.py‘ is the software call

‘-i ./False-ECG-sinus.csv‘ is the way to call input data

‘-w 500’ is defining the width of the window used to evaluate one PeEn value

‘-d 3’ is dimension (number of used points used to find their ordering)

‘-e 1’ is a lag in between used points


******************************************************************************
Examples of the program use:
******************************************************************************
run examples: 

* python3 PeEn-run-20260206.py -i ./False-ECG-sinus.csv -w 500 -d 3 -e 1

* python3 PeEn-run-20260206.py -i ./False-ECG-sinus-jumps.csv -w 500 -d 3 -e 1

* python3 PeEn-run-20260206.py -i ./False-ECG-modul-sinus.csv -w 500 -d 5 -e 10

* python3 PeEn-run-20260206.py -i ./False-Lorenz-attractor.csv -w 500 -d 3 -e 1
******************************************************************************
******************************************************************************


******************************************************************************
Generation of used data samples:
******************************************************************************
* python3 Generator-false-ECG-260205.py

* python3 Generator-false-ECG-jumps-260205.py

* python3 Generator-false-ECG-modul-sinus-260205.py

* python3 Generator-Lorenz-attractor-20260205.py

******************************************************************************
******************************************************************************


