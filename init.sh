#! /bin/bash

python -u main.py | /home/jikaczmarski/go/bin/asciigraph -r -lb 0 -ub 20 -h 60 -w 200 -f 60 -sn 2 -sc "blue,red" -sl "Voltage (V), Current (A)"
