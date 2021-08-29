import sys
from collections import deque
input = sys.stdin.readline
paper =deque(list(input().strip()))
word = list(input().strip())
stack = []
cnt = 0
while paper :
    val = paper.popleft()
    stack.append(val)
    if len(stack) >= len(word) :
        if stack[-len(word):] == word :
            stack = []
            cnt += 1
print(cnt)