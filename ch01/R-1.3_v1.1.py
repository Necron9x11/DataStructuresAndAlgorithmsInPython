#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise R-1.3
#
# Write a short Python function, minmax(data), that takes a sequence of 
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution. 
#
# Author: Daniel Raphael
#
# NOTE: This works but it is unnecessarily complicated as I pass in the list of numbers as a string and \
        # then use the split function to convert the string to a list and then a for loop to convert \
        # each element of the list from a string to an int. 
        #
        # It was a useful exercise but there is a simpler solution. 

import argparse
import sys

# Configure flag to turn debug statement output on/off. Set to True to enable debugging and False to disable it. 
DEBUG = True

# Configure argument parser
parser = argparse.ArgumentParser('Takes one argument, "data" which is a list of numbers of any length >= 2. Returns a tuple of length 2 containing the smallest and largest number in the set.')
parser.add_argument("data", help="a list of >= 2 numbers .")
args = parser.parse_args()

# Display proof that the cli argument is passed in as a string. 
if DEBUG:
    print('\nDBG: {} passed into "args.data" from command line'.format(args.data))
    print('DBG: As passed in, the argument "data" is type {}'.format(type(args.data)))

# Convert argument data, passed in as a string, to a list. Splitting the input data on the delimiter and storing
# the results in a new variable creates a list. When I tried this with list(args.data) 
# and then sorted it I ended up with:
#
# [',', ',', ',', ',', ',', ',', ',', ',', ',', '0', '1', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# TODO: Figure out why the above is happening. 
#

# Split the input into a list. Current valid input dleimiters are " " or ",". 
# If input is improperly delimited alert the user and exit the program.
# This really is not sufficient as "10|3|5|7|1|11|51|16" triggers the else clause 
# but "10 | 3 | 5 | 7 | 1 | 11 |51 |16" will raise an exception:
#
# Traceback (most recent call last):
#   File "./R-1.3_v1.py", line 67, in <module>
#       print(minmax(some_list_data))
#   File "./R-1.3_v1.py", line 63, in minmax
#       data_in = [int(x) for x in data_in]
#   File "./R-1.3_v1.py", line 63, in <listcomp>
#       data_in = [int(x) for x in data_in]
# ValueError: invalid literal for int() with base 10: '|'
#
# So better error handling is needed.  
#
# Also check that there are at least two numbers supplied on the cli. 

if ',' in args.data:
    some_list_data = args.data.split(',')
elif ' ' in args.data:
    some_list_data = args.data.split(' ')
else:
    print('Input must be a list of numbers delimited either by commas or by spaces')
    sys.exit()

# This is not really needed as due to the above delimiter checks it is not possible to input
# less than two numbers
#
# if len(some_list_data) < 2:
#    print('>= 2 numbers required as input')

if DEBUG:
    print('\nDBG: Variable some_list_data, created with "list(args.data) is type {}"'.format(type(some_list_data)))
    print('DBG: Variable some_list_data == {}'.format(some_list_data))
    print('DBG: Length of some_list_data is {}'.format(len(some_list_data)))

# Define a function to take the list "data" and sort it so we can determine the min and max values. 
# Then use a simultaneous assignment statement to automatically pack a tuple with the first and last
# list elements which, after sorting, will be the min and max values.

def minmax(data_in):
    if DEBUG:
        print('\nDBG: Data passed into "minmax()" is type {}'.format(type(data_in))) 
        data_in.sort()
        print('DBG: Result of "data_in.sort()" is {}'.format(data_in))
        print('DBG: Elements in list are curently type {}'.format(type(data_in[0])))
    data_in = [int(x) for x in data_in]
    data_in.sort()
    lowhigh = data_in[0],data_in[-1]
    if DEBUG:
        print('\nDBG: Convert list elements to type int with: "data_in = [int(x) for x in data_in]"'.format())
        print('DBG: After conversion elements in list are type {}'.format(type(data_in[0])))
    return lowhigh

print(minmax(some_list_data))

