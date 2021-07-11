import sys
input = sys.stdin.readline

N,M,K,X = map(int,input().split())
# N : 도시의 갯수
# M : 도로의 갯수
# K : 거리 정보
# X : 출발 도시의 번호
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b) # 단방향 그래프

visit = [0] * (N+1)
visit[X] = 1

from collections import deque
q = deque([X])

step = [0]*(N+1)

while q :
    x = q.popleft()
    visit[x] = 1
    for i in graph[x] :
        if visit[i] == 0 :
            visit[i] = 1
            step[i] = step[x] + 1
            q.append(i)
if K not in step :
    print(-1)
    sys.exit(0)

for i,v in enumerate(step):
    if v == K :
        print(i)
