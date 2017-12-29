#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise R-1.9 version 1
#
# What parameters should be sent to the rnage constructor, to produce a
# range with values 50, 60, 70, 80?
#
# Author: Daniel Raphael
#

import argparse
import sys

# Configure argument parser
parser = argparse.ArgumentParser('Accepts no input. Generates a predefined series of numbers using the range function.')
# parser.add_argument("n", type=int, help="a positive integer.")
parser.add_argument("-d", "--debug", action="store_true", help="include to enable debugging")
args = parser.parse_args()

def create_prescribed_range():
    my_list =[]
    # Tried to use a combination of list and range comprehension syntax here but I am still missing some 
    # comprehension around it apparently. 
    # TODO: Figure out how to make this work with comprehension syntax. How can I iterate through a range and 
    #       populate a list using comprehension syntax?
    #
    #(my_list.append(x) for x in range(50, 90, 10))
    #
    for x in range(50, 90, 10):
        my_list.append(x)

    if args.debug:
        print('DBG: Length of my_list is {}'.format(len(my_list)))
        for num in my_list:
            # have to use the list's .index method here to get the index of each number as it is not a 1:1 
            # relationship. The first number in the sequence is 50, but it's index is 0. 
            print('my_list[{}] == {}'.format(my_list.index(num),num ))
            #print(num)

    return my_list

if __name__ == '__main__':
    print(create_prescribed_range())
