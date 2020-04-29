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
print("="*24+" LAB-RESULTS "+"="*24)
# IMPORTS BELLOW
#   Statments we use to open different modules that people have built. 
#   This allows code to be reusable, which is a key factor to good 
#   programming and performance.

# END OF IMPORTS

# START OF CODE BLOCK
"""
TASKING:
    Perfrom the following on the variable `dataStr`:
    1) Set `dataStr` value to 'opensource.com'
    2) Set `dataStrFull` full value of `https://` and use the `dataStr` to create this variable
    3) Set `dataStrSplit` to the value of `dataStrFull` split on the the character `.`, into a list using a string method (*HINT: Python Docs*)
    4) Try to print `dataStrSplit` with the format string methods like `print('{} {}'.format('one', 'two'))`
"""















# END OF CODE BLOCK

# ----- DO NOT EDIT BELLOW THIS LINE -----
from colorama import init
from termcolor import colored
import os
 
init(autoreset=True)

def test_dataStr():
    try:
        v = 'dataStr is set'
        if str(dataStr) and str(dataStr) == 'opensource.com':
            print("%s: %s" % (v, colored('PASS', 'green')))
        else:
            print("%s: %s" % (v, colored('FAIL', 'red')))
    except NameError:
        print("%s: %s" % (v, colored('FAIL', 'red')))

def test_dataStrFull():
    try:
        v = 'dataStrFull is set'
        if str(dataStrFull) and str(dataStrFull) == 'https://opensource.com':
            print("%s: %s" % (v, colored('PASS', 'green')))
        else:
            print("%s: %s" % (v, colored('FAIL', 'red')))
    except NameError:
        print("%s: %s" % (v, colored('FAIL', 'red')))

def test_dataStrSplit():
    try:
        v = 'dataStrSplit is set and the correct split'
        if list(dataStrSplit) and dataStrSplit[1] == 'com' :
            print("%s: %s" % (v, colored('PASS', 'green')))
        else:
            print("%s: %s" % (v, colored('FAIL', 'red')))
    except NameError:
        print("%s: %s" % (v, colored('FAIL', 'red')))

if __name__ == "__main__":
    test_dataStr()
    test_dataStrFull()
    test_dataStrSplit()