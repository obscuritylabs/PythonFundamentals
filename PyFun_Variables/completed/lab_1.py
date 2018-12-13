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
# imports: things we use to open diffrent modules that people have built
#           This allows code to be reusable, which is a key factor to good
#           programing and performance. 
import os
# END OF IMPORTS

# START OF CODE BLOCK
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

# END OF CODE BLOCK

# ----- DO NOT EDIT BELLOW THIS LINE -----
from colorama import init
from termcolor import colored
import os

init(autoreset=True)

# check if program name is defined
try:
    if str(currentProgram) and str(currentProgram) == 'lab-1.py':
        print("Program name is defined: %s" % (colored('PASS', 'green')))
    else:
        print("Program name is defined: %s" % (colored('FAIL', 'red')))
except NameError:
    print("Program name is defined: %s" % (colored('FAIL', 'red')))
    
# check if program pid is defined
try:
    if int(currentPid) and int(currentPid) == os.getpid():
        print("Program PID is defined: %s" % (colored('PASS', 'green')))
    else:
        print("Program name is defined: %s" % (colored('FAIL', 'red')))
except NameError:
    print("Program name is defined: %s" % (colored('FAIL', 'red')))
