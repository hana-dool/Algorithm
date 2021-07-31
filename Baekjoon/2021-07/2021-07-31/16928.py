import sys
input = sys.stdin.readline
from collections import deque

q = deque([])
T = int(input())
for _ in range(T):
    N,M = map(int,input().split()) # N 은 문서의 갯수 / # M 에서 몇번쨰에 놓여있는지
    lst = list(map(int,input().split()))
    lst = list(zip(lst,list(range(N))))
    q = deque(lst)
    idx = 0
    while q :
        mx = max(q,key = lambda x : x[0])[0]
        val = q.popleft()
        if q :
            if val[0] == mx :
                idx += 1
                if val[1] == M :
                    print(idx)
                    break
            else :
                q.append(val)
        else :
            idx += 1
            print(idx)



