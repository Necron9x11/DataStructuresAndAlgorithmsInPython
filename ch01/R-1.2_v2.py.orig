#!/usr/bin/env python3
# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplicatoin, modulo, or division operators. 

import argparse

parser = argparse.ArgumentParser('Takes one argument, k. Returns True if k is even,  False if k is not even.')
parser.add_argument("k", help="an integer.")
args = parser.parse_args()

some_number_k = int(args.k)

def is_even(k):
    while k > 0: 
        k -= 2
    if k < 0:
        return False
    else:
        return True

print(is_even(some_number_k))

