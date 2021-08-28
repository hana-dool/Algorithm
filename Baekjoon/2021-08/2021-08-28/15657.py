import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
for i in list(combinations_with_replacement(lst,M)) :
    print(*i)
