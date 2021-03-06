# PYTHON METADATA BELLOW
'''
    File name: lab-1.py
    Author: Alexander Rymdeko-Harvey
    Date created: 12/12/2018
    Date last modified: 12/12/2018
    Python Version: 3.6.5
    License: 
        Copyright (c) 2018 Alexander Rymdeko-Harvey & Obscurity Labs LLC.

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
import os
# END OF IMPORTS

# START OF LAB CODE BLOCK
"""
TASKING:
    Take the time to create two key variables, currentProgram which is a string
    that you define of the current program name. Second the use the python builtin
    os module to get current process id (PID). print both to the console using any
    method you would like to use.
"""

currentProgram = 'lab-1.py'

currentPid = os.getpid()

print("current program: %s" % (currentProgram))
print("current PID: %d" % (currentPid))

# END OF LAB CODE BLOCK

# ----- DO NOT EDIT BELLOW THIS LINE -----
from colorama import init
from termcolor import colored
import os

init(autoreset=True)
# print test harness
print("="*20+" TEST-HARNESS-RESULTS "+"="*20)

# check if program name is defined
def test_program_name():
    try:
        if str(currentProgram) and str(currentProgram) == 'lab-1.py':
            print("Program name is defined: %s" % (colored('PASS', 'green')))
        else:
            print("Program name is defined: %s" % (colored('FAIL', 'red')))
    except NameError:
        print("Program name is defined: %s" % (colored('FAIL', 'red')))

# check if program pid is defined
def test_program_pid():
    try:
        if int(currentPid) and int(currentPid) == os.getpid():
            print("Program PID is defined: %s" % (colored('PASS', 'green')))
        else:
            print("Program name is defined: %s" % (colored('FAIL', 'red')))
    except NameError:
        print("Program name is defined: %s" % (colored('FAIL', 'red')))

if __name__ == "__main__":
    test_program_name()
    test_program_pid()
