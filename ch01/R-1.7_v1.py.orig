#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise R-1.5 version 1
#
# Give a single command that computes the sum from Exercise R-1.4, relying on Python's 
# comprehension syntax and the built-in sum function.  
#
# As a reminder, here is the exercise R-1.4 description again:
#
#   Write a short Python function that takes a positive integer n and returns the sum of the squares 
#   of all the positive integers smaller than n. 
#
# Author: Daniel Raphael
#

import argparse
import sys

# Configure argument parser
parser = argparse.ArgumentParser('Takes one positive number as the argument "n". Returns the sum of the squares of all positive integers smaller than n.')
parser.add_argument("n", type=int, help="a positive integer.")
parser.add_argument("-d", "--debug", action="store_true", help="include to enable debugging")
args = parser.parse_args()

def sumofsquaresof(number):
    # 
    # This uses Python's comprehension syntax to create a for loop that runs on a range statement 
    # which uses the number passed in as the high end of the range. 
    # 
    # Comprehension syntax is based on 
    # Set Builder notation: https://en.wikipedia.org/wiki/Set-builder_notation
    #
    # This site's explanaiton of Python List Comprehension syntax gave me the visual I needed to 
    # switch on the lightbulb: 
    #   http://carlgroner.me/Python/2011/11/09/An-Introduction-to-List-Comprehensions-in-Python.html
    #
    return sum(x**2 for x in range (1, number))

if __name__ == '__main__':
    print('The sum of the squares of all numbers from 1 to {} is {}'.format(args.n, sumofsquaresof(args.n)))
