import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    s_1 = set(s1)
    s_2 = set(s2)
    val = s_1 & s_2
    # Write your code here
    if val :
        print("YES")
    else :
        print('NO')

twoStrings('hi', 'world')