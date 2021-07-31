import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1) # N 은 문제의 수

for _ in range(M) :
    start , end = map(int,input().split())
    graph[start].append(end)
    indegree[end] += 1

q = []
rst = []
for i in range(1,N+1) :
    if indegree[i] == 0 :
        heapq.heappush(q,i)

while q :
    now = heapq.heappop(q)
    rst.append(now)
    for i in graph[now] :
        indegree[i] -= 1
        if indegree[i] == 0 :
            heapq.heappush(q,i)

print(*rst)

