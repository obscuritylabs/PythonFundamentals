# PYTHON METADATA BELLOW
'''
    File name: lab-1.py
    Author: Alexander Rymdeko-Harvey
    Date created: 12/12/2018
    Date last modified: 12/12/2018
    Python Version: 3.6.5
    License: 
        Copyright (c) 2018 ⭕Alexander Rymdeko-Harvey & Obscurity Labs LLC.

        This file is part of Python Fundementals (3.6)
        (see https://github.com/obscuritylabs).

        License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
'''
# END OF METADATA

# IMPORTS BELLOW
#   Statments we use to open different modules that people have built. 
#   This allows code to be reusable, which is a key factor to good 
#   programming and performance.

# END OF IMPORTS

# START OF CODE BLOCK
"""
TASKING:
    Perfrom the following on the variable `dataNum`:
    1) Set Value to `1.2299`
    2) Set `dataNumPower` to power of 2 for `dataNum`
    3) Set `dataNum2` to the int `10`
    4) Set `dataNum2Bytes` to the bytes of `dataNum2`, setting the length to `1` and the byte order to `big`
"""

dataNum = 1.2299
dataNumPower = pow(dataNum, 2)
dataNum2 = 10
dataNum2Bytes = dataNum2.to_bytes(1, byteorder='big')

# END OF CODE BLOCK

# ----- DO NOT EDIT BELLOW THIS LINE -----
from colorama import init
from termcolor import colored
import os
 
init(autoreset=True)

try:
    v = 'dataNum is set'
    if float(dataNum) and float(dataNum) == 1.2299:
        print("%s: %s" % (v, colored('PASS', 'green')))
    else:
        print("%s: %s" % (v, colored('FAIL', 'red')))
except NameError:
    print("%s: %s" % (v, colored('FAIL', 'red')))

try:
    v = 'dataNum2 is set'
    if int(dataNum2) and int(dataNum2) == 10:
        print("%s: %s" % (v, colored('PASS', 'green')))
    else:
        print("%s: %s" % (v, colored('FAIL', 'red')))
except NameError:
    print("%s: %s" % (v, colored('FAIL', 'red')))

try:
    v = 'dataNumPower is set and the correct power'
    if float(dataNumPower) and float(dataNumPower) == 1.5126540099999999:
        print("%s: %s" % (v, colored('PASS', 'green')))
    else:
        print("%s: %s" % (v, colored('FAIL', 'red')))
except NameError:
    print("%s: %s" % (v, colored('FAIL', 'red')))

try:
    v = 'dataNum2Bytes is set and the correct bytes'
    if bytes(dataNum2Bytes) and bytes(dataNum2Bytes) == b'\n':
        print("%s: %s" % (v, colored('PASS', 'green')))
    else:
        print("%s: %s" % (v, colored('FAIL', 'red')))
except NameError:
    print("%s: %s" % (v, colored('FAIL', 'red')))