#!/usr/bin/env python3
# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is n = mi for some 
# integer i, and False otherwise. 

import sys
import argparse

# n = int(sys.argv[1])
# m = int(sys.argv[2])

parser = argparse.ArgumentParser('Takes two arguments, n & m. Returns True if n in a multiple of m and False if n is not a multiple of n')
parser.add_argument("n", help="an integer.")
parser.add_argument("m", help="an integer.")
args = parser.parse_args()

def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False

print(is_multiple(int(args.n), int(args.m)))

