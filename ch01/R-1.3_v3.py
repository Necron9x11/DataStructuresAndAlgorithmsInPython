#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise R-1.3 version 3
#
# Write a short Python function, minmax(data), that takes a sequence of 
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution. 
#
# Author: Daniel Raphael
#

import argparse
import sys

# Configure argument parser
parser = argparse.ArgumentParser('Takes one argument, "data" which is a list of numbers of any length >= 2. Returns a tuple of length 2 containing the smallest and largest number in the set.')
parser.add_argument("data", type=int, nargs="+", help="a list of >= 2 numbers .")
parser.add_argument("-d", "--debug", action="store_true", help="include to enable debugging")
parser.add_argument("-df", "--debug_function", action="store_true", help="include to enable debugging")
args = parser.parse_args()

# Make sure there were at least two numbers supplied as arguments on the cli. 
if len(args.data) < 2:
    print('Two or more numbers required as argumets')
    sys.exit()

# Define a function to take the list "data" and sort it so we can determine the min and max values. 
# Then use a simultaneous assignment statement to automatically pack a tuple with the first and last
# list elements which, after sorting, will be the min and max values.

def minmax(data_in):
    data_in.sort()
    #lowhigh = data_in[0],data_in[-1]
    #return lowhigh
    return (data_in[0],data_in[-1])

print(minmax(args.data))

