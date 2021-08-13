# 위상정렬이네..?
from collections import deque
import sys
input = sys.stdin.readline

N , M = map(int,input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split()) # A->B
    indegree[B] += 1
    graph[A].append(B)


q = deque([])
for i in range(1,N+1) :
    if indegree[i] == 0 :
       q.append(i)

rst = []
while q :
    now = q.popleft()
    rst.append(now)
    for i in graph[now] :
        indegree[i] -= 1
        if indegree[i] == 0 :
            q.append(i)
print(*rst)