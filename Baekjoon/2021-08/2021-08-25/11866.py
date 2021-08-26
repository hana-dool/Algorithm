import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
lst = list(range(1,N+1))
lst = deque(lst)
ans  = [ ]
cnt = 0
while lst :
    val = lst.popleft()
    cnt += 1
    if cnt % K == 0:
        ans.append(val)
    else :
        lst.append(val)
ans_str =', '.join(map(str,ans))
print(f'<{ans_str}>')