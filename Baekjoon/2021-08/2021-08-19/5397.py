import sys
input = sys.stdin.readline

T = int(input())
# <BAC<<F>D-G

# BAC

# BA
# C

# B
# AC

# BF
# AC

# < 를 만나면 , stack1 에 있는 값을 stack2 에 appendleft
# > 를 만나면   stack 2 에 있는 값을 stack 2 에 append

from collections import deque
for _ in range(T) :
    stack1 = []
    stack2 = deque([])
    strng = input().rstrip()
    for i in strng :
        if i == '<' :
            if stack1 :
                stack2.appendleft(stack1.pop())
        elif i == '>' :
            if stack2 :
                stack1.append(stack2.popleft())
        elif i == '-' :
            if stack1 :
                stack1.pop()
        else :
            stack1.append(i)
    ans=stack1+list(stack2)
    print(''.join(ans))




