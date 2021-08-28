import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
move = list(map(int,input().split()))
balloon = list(range(1,N+1))
lst = deque(list(zip(balloon,move)))
ans = deque([])
while True :
    answer = lst.popleft()
    ans.append(answer)
    if not lst :
        break
    if answer[1] >= 1 :
        for _ in range(answer[1]-1) :
            lst.append(lst.popleft())
    elif answer[1] <= -1 :
        for _ in range(abs(answer[1])) :
            lst.appendleft(lst.pop())

print(*list(map(lambda x : x[0],ans)))
