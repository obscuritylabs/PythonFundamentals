# PYTHON METADATA BELLOW
'''
    File name: lab-2.py
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
import sys
# END OF IMPORTS

# START OF CODE BLOCK
"""
TASKING:
    Take the time to create two variables that will be used in the future projects. import the module `sys` and 
    use it to get the current modules loaded in the current namespace for debug purposes. Please name this variable 
    `systemMod` and than convert this variable to a string which will be placed into `systemModS`.
"""













# END OF CODE BLOCK

# ----- DO NOT EDIT BELLOW THIS LINE -----
from colorama import init
from termcolor import colored
import os

init(autoreset=True)

# check if program name is defined
def test_program_name():
    try:
        if systemMod:
            print("systemMod name is defined: %s" % (colored('PASS', 'green')))
        else:
            print("systemMod name is defined: %s" % (colored('FAIL', 'red')))
    except NameError:
        print("systemMod name is defined: %s" % (colored('FAIL', 'red')))
    
# check if program pid is defined
def test_program_pid():
    try:
        if systemModS:
            print("systemModS name is defined: %s" % (colored('PASS', 'green')))
        else:
            print("systemModS name is defined: %s" % (colored('FAIL', 'red')))
    except NameError:
        print("systemModS name is defined: %s" % (colored('FAIL', 'red')))

# check if dict
def test_dict():
    try:
        if isinstance(systemMod, dict):
            print("systemMod is defined as a Dict: %s" % (colored('PASS', 'green')))
        else:
            print("systemMod is defined as a Dict: %s" % (colored('FAIL', 'red')))
    except NameError:
        print("Program name is defined: %s" % (colored('FAIL', 'red')))

# check if str
def test_str():
    try:
        v = 'systemModS is defined as a Str'
        if isinstance(systemModS, str):
            print("%s: %s" % (v, colored('PASS', 'green')))
        else:
            print("%s: %s" % (v, colored('FAIL', 'red')))
    except NameError:
        print("%s: %s" % (v, colored('FAIL', 'red')))

if __name__ == "__main__":
    test_program_name()
    test_program_pid()
    test_dict()
    test_str()