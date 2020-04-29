#!/usr/bin/env python3
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
import os
# END OF IMPORTS

# START OF LAB CODE BLOCK

def hello_world(value):
    if value == 5:
        return 'pass'
    return 'fail'









# END OF LAB CODE BLOCK

# ----- DO NOT EDIT BELLOW THIS LINE -----
from colorama import init
from termcolor import colored
import os

init(autoreset=True)
# print test harness
print("="*20+" TEST-HARNESS-RESULTS "+"="*20)

# check if program name is defined
def test_hello():
    try:
        hello_world(1)
        print("hello world is present: %s" % (colored('PASS', 'green')))
    except Exception as e:
        print("hello world is NOT present: %s" % (colored('FAIL', 'red')))

def test_hello_string():
    try:
        x = hello_world(5)
        if x != 'pass':
            raise
        print("hello world if statement works: %s" % (colored('PASS', 'green')))
    except Exception as e:
        print("hello world if statement does NOT work: %s" % (colored('FAIL', 'red')))

if __name__ == "__main__":
    test_hello()
    test_hello_string()

