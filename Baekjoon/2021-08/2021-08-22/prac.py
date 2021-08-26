N = int(input())
lst = list(map(int,input().split()))
from collections import deque

stack = []
for idx, val in enumerate(lst) :
    if val == 0 :
        stack.append(idx+1)
    else :
        stack.insert(-1*val,idx+1)
print(*stack)