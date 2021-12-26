#!/bin/python3
#capitalizing 1st word for every word in a sentence
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
            
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
