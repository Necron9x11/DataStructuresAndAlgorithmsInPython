#!/usr/bin/env python3

# Data Structures & Algorithms in Python - Goodrich
# Chapter 1 | Exercise C-1.14 version 1
#
# Write a short Python function that takes a sequence of numbers and determines if there is a distinct
# pair of numbers in the sequence whose product is odd. 
#
# Author: Daniel Raphael
#
# TODO: This is incomplete. Mostly just testing to visualize the itertools.combinations() function. 
#       This is the first time I have used a fucntion from the itertools module. It works as I expected - 
#       just like any other Python iterable. It creates r length subsequences of elements from the 
#       input iterable.
#
#       Basically it is a mess and needs to be cleaned up. Also the instrunctions are not clear to me. 
#       How does one programatically identify a distinct pair if "distinct" means "easily identifiable". 
#       But, in this context, based on what traits? It would make more sense to me if the instructions 
#       had been to identify *unique* pairs. 
#
#       At any rate, as it stands now the code will generate a list of all the odd numbers that can possibly
#       be produced by multiplying every possible combination of any list of numbers supplied as command 
#       line arguments to the script when it is run. 
#
#       Currenlty none of the code is encapsulated in a function yet but it spits out a both a list containing 
#       all of the odd products as well as a string containing the odd products. None of the code is 
#       encapsulated in a function yet. 

import argparse
import sys
import itertools

# Configure argument parser
parser = argparse.ArgumentParser('takes as input a series of numbers and determines if there is a distinct pair whose product is odd')
parser.add_argument("number_list", type=int, nargs="+", help="a positive integer.")
parser.add_argument("-d", "--debug", action="store_true", help="include to enable debugging")
args = parser.parse_args()

# Testing itertools.combinations()
#
all_combinations = [list(x) for x in itertools.combinations(args.number_list, 2)]
if args.debug:
    print('DBG: all_combinations == {}'.format(all_combinations))
odd_products = []
for pair in all_combinations:
    x, y = pair
    result = x*y
    if result % 2 != 0:
        odd_products.append(result)
    if args.debug:
        print('DBG: {} * {} = {}'.format(x,y,result))
        print('DBG: Result == {}'.format(result))
        print('DBG: {} % 2 == {}'.format(result, result % 2))

if args.debug:
    for odd in odd_products:
        print('DBG: odd_products[{}] == {}'.format(odd_products.index(odd), odd))

print('final list of odd products as string == {}'.format(' '.join(str(p) for p in odd_products)))
print('final list of odd products as list == {}'.format(odd_products))

def find_odd_product(some_numbers):

    return some_numbers

if __name__ == '__main__':
   #  print('Function was passed {} of type {}'.format(find_odd_product(args.number_list), type(find_odd_product(args.number_list))))

    if args.debug:
        print('Function was passed {} of type {}'.format(find_odd_product(args.number_list), type(find_odd_product(args.number_list))))
