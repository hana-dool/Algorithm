import sys
read = sys.stdin.readline
N,M = map(int,read().split())
order = list(map(int,read().split()))

from collections import deque
lis = list(range(1,N+1))
dq = deque(lis)
cnt = 0

for v in order :
    idx = dq.index(v)
    if idx+1 > (len(dq)//2)+1 : # 오른쪽으로 계속 가야한다.
        dq.rotate(len(dq)-idx)
        cnt += (len(dq)-idx)
        dq.popleft()
    else :
        dq.rotate(-idx)
        dq.popleft()
        cnt += idx

print(cnt)