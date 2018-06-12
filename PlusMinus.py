#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal as D


# Complete the plusMinus function below.
def plusMinus(arr):
    # arr=[ -4,3,0,-9,4,1]
    p,n,z=0,0,0
    for i in arr:
        if i>0:
            p=p+1
        elif i<0 :
            n= n+1
        else:
            z=z+1
    print(p/(p+n+z))
    print(n/(p+n+z))
    print(z/(p+n+z))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
