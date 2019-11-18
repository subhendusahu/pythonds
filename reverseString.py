#!/usr/bin/python3 

import sys

def reverse(string_to_reverse):
    return string_to_reverse[::-1]

print(reverse(sys.argv[1]))
