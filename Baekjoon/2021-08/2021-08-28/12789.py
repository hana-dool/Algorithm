import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
q = deque(list(map(int,input().split())))
wait = []
line = []
while q :
    now = q.popleft()
    if line and wait :
        while line :
            if wait[-1] + 1 == line[-1] :
                wait.append(line.pop())
            else :
                break
    if not wait :
        if now == 1 :
            wait.append(now)
        else :
            line.append(now)
    else :
        if wait[-1] + 1 == now :
            wait.append(now)
        else :
            line.append(now)

final = wait + line[::-1]
if final == list(range(1,N+1)) :
    print("Nice")
else :
    print('Sad')
