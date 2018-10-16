#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise R-1.4 version 2
#
# Write a short Python function that takes a positive integer n and returns the sum of the squares 
# of all the positive integers smaller than n. 
#
# Author: Daniel Raphael
#

import argparse
import sys

# Configure argument parser
parser = argparse.ArgumentParser('Takes one positive number as the argument "n". Returns the sum of the squares of all positive integers smaller than n')
parser.add_argument("n", type=int, help="a positive integer.")
parser.add_argument("-d", "--debug", action="store_true", help="include to enable debugging")
args = parser.parse_args()

if args.n < 1:
    print('n must be a positive integer greater than zero')
    sys.exit()

def sumofsquaresof(number):
    total_of_all_squares = 0        # holds the sum of all squares of all numbers

    # loop through a range of numbers from 1 to args.n+1 and 
    # add the square of each number to total_of_all_squares.
    # 
    # return the sum of all squares
    #
    for num in range(1, number):
        total_of_all_squares += num**2

    return total_of_all_squares

if __name__ == '__main__':
    print('The sum of the squares of all numbers from 1 to {} is {}'.format(args.n, sumofsquaresof(args.n)))

