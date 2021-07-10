import sys
import heapq
input = sys.stdin.readline



V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
inf = 10**9
distance = [inf] * (V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
q = []
def dijkstra(start):
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q :
        d,s = heapq.heappop(q)
        if distance[s] < d :
            continue
        else :
            for i in graph[s]:
                cost = d + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
dijkstra(K)
for j in distance[1:]:
    if j != inf:
        print(j)
    else :
        print('INF')