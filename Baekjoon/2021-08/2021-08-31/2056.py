import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

ans = [0]*(N+1)

def topology() :
    q = deque()
    for idx in range(1,N+1) :
        if indegree[idx] == 0 :
            q.append((idx,1))
    while q :
        now ,cnt = q.popleft()
        ans[now] = cnt
        for end in graph[now] :
            indegree[end] -= 1
            if indegree[end] == 0 :
                q.append((end,cnt+1))
topology()
print(*ans[1:])