#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise R-1.4 version 1
#
# Write a short Python function that takes a positive integer n and returns the sum of the squares 
# of all the positive integers smaller than n. 
#
# Author: Daniel Raphael
#

import argparse
import sys

DEBUG = True

# Configure argument parser
parser = argparse.ArgumentParser('Takes one positive number as the argument "n". Returns the sum of the squares of all positive integers smaller than n')
parser.add_argument("n", type=int, help="a positive integer.")
parser.add_argument("-d", "--debug", action="store_true", help="include to enable debugging")
args = parser.parse_args()

if args.n < 1:
    print('n must be a positive integer greater than zero')
    sys.exit()

# This is me overthinking it. Plus I just really wanted to use a range to create a list and then 
# iterate through the list to compute the sum of all the squares. 
# 
# I will clean this up and collapse it down to one for loop in the next version. 
def sumofsquaresof(number):
    number_series = []              # to hold each number from 1 to n 
    total_of_all_squares = 0        # holds the sum of all squares of all numbers

    # loop through a range of numbers from 1 to args.n and append each number to the list number_series.
    # 
    for num in range(1, number):
        number_series.append(num)
    if args.debug:
        print('number_series == {}'.format(number_series))
    
    # loop through number_series and add the square of each number to total_of_all_squares.
    # 
    # return the sum of all squares
    #
    for num in number_series:
        total_of_all_squares += num**2
        if args.debug:
            print('{}^2 == {}'.format(num, num**2))
            print('total of all squares so far == {}\n'.format(total_of_all_squares))

    print('Output:')
    return total_of_all_squares

if __name__ == '__main__':
    print(sumofsquaresof(args.n))

