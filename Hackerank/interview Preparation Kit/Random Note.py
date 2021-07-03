import math
import os
import random
import re
import sys

def checkMagazine(magazine, note):
    dic = {}
    for i in magazine:
        dic[i] = dic.get(i,0) + 1
    for i in note:
        dic[i] = dic.get(i,0) - 1
    if min(list(dic.values())) < 0 :
        return('No')
    else :
        return('Yes')

if __name__ == '__main__' :
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    print(checkMagazine(magazine, note))
