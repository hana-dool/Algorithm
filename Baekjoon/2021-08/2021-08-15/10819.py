import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
lst.sort()
l = len(lst)



def cal(lst):
    cnt = 0
    for i in range(l-1) :
        cnt += abs(lst[i+1] - lst[i])
    return cnt
mx = 0
for i in list(permutations(lst)) :
    mx = max(mx,cal(list(i)))
print(mx)