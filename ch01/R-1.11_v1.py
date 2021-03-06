#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise R-1.11 version 1
#
# Demonstrate how to use Python's list comprehension syntax to produce the list
# [1, 2, 4, 8, 16, 32, 64, 128, 256]
#
# Author: Daniel Raphael
#

import argparse

# Configure argument parser
parser = argparse.ArgumentParser('Accepts no input. Generates a predefined series of numbers using the range function.')
parser.add_argument("-d", "--debug", action="store_true", help="include to enable debugging")
args = parser.parse_args()

def create_prescribed_range():
    my_list = [2**i for i in range(9)]

    return my_list

if __name__ == '__main__':
    print(create_prescribed_range())
