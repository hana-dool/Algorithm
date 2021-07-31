
import sys
from collections import deque
input = sys.stdin.readline
V, E = map(int,input().split())

indegree = [0]*(V+1)
graph = [[] for _ in range(V+1)]

for _ in range(E) :
    start, end = map(int,input().split())
    graph[start].append(end)
    indegree[end] += 1

q = deque()
rst = []
for i in range(1,V+1) :
    if indegree[i] == 0 :
        q.append(i)
        rst.append(i)

while q :
    now = q.pop()
    for e in graph[now]:
        indegree[e] -= 1
        if indegree[e] == 0 :
            q.append(e)
            rst.append(e)
print(rst)
