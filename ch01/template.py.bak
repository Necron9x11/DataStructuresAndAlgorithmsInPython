#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise R-1.12 version 1
#
# Python's random module includes a function choice(data) that returns a random element from a 
# non-empty sequence. The random module includes a more basic function randrange, with parameterization 
# similar to the built-in range function, that return a random choice from the given range. 
# Using only the randrange function, implement your own version of the choice function. 
#
# Author: Daniel Raphael
#

import argparse
import sys
import random

# Configure argument parser
parser = argparse.ArgumentParser('Takes one positive number as the argument "n". Returns the sum of the squares of all positive integers smaller than n')
# parser.add_argument("n", type=int, help="a positive integer.")
parser.add_argument("-d", "--debug", action="store_true", help="include to enable debugging")
args = parser.parse_args()

# Currnetly this simply demonstrates the use of the random.choice() function by using a list comprehension to 
# seed a list, called twenty_sided_die. This list is then passed to random.choice() to simulate the roll of a 
# twenty sided die. 
#
# TODO: Go read up on the random.randrange() function so as to be able to use it to simulate the 
#       random.choice() function. 
#
def twenty_sided_die():
    die_numbers = [x for x in range(1,21)]
    my_roll = random.choice(die_numbers)
    if args.debug:
        print('die_numbers == {}'.format(die_numbers))
        print('my_roll == {}'.format(my_roll))

    return my_roll

if __name__ == '__main__':
    print('You rolled a {}'.format(twenty_sided_die()))

