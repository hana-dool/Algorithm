import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for i in range(N) :
    lst = list(map(int,input().split()))
    time = lst[0]
    prior = lst[2:]
    graph[i+1].extend(prior)
    indegree[i+1] = len(prior)


q = deque()
rst = []
for i in range(1,N+1):
    if indegree[i] == 0 :
        q.append(i)
while q :
    now = q.popleft()
    rst.append(now)
    for i in graph[now] :
        indegree[i] -= 1
        if indegree[i] == 0 :
            q.append(i)
print(rst)