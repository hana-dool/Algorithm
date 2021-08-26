N = int(input())
lst = list(map(int,input().split()))
from collections import deque

stack = []
for idx, val in enumerate(lst) :
    stack.insert(-1*val,idx+1)
print(*stack)