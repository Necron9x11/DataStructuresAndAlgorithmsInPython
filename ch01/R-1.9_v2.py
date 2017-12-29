#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise R-1.9 version 2
#
# What parameters should be sent to the rnage constructor, to produce a
# range with values 50, 60, 70, 80?
#
# Author: Daniel Raphael
#

import argparse

# Configure argument parser
parser = argparse.ArgumentParser('Accepts no input. Generates a predefined series of numbers using the range function.')
parser.add_argument("-d", "--debug", action="store_true", help="include to enable debugging")
args = parser.parse_args()

def create_prescribed_range():
    my_list = [x for x in range(50, 90, 10)]

    if args.debug:
        print('DBG: Length of my_list is {}'.format(len(my_list)))
        for num in my_list:
            # have to use the list's .index method here to get the index of each number as it is not a 1:1 
            # relationship. The first number in the sequence is 50, but it's index is 0. 
            print('my_list[{}] == {}'.format(my_list.index(num),num ))

    return my_list

if __name__ == '__main__':
    print(create_prescribed_range())
