import sys
import heapq
input = sys.stdin.readline
inf = 10**9

V, E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [inf] * (V+1)

for _ in range(E) :
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
q = []


def dijkstra(start) :
    heapq.heappush(q,(0,start)) # 거리 , 시작점
    distance[start] = 0
    while q :
        dis, now = q.pop()
        if distance[now] < dis :
            continue
        else :
            for i in graph[now] : # i 는 (v(정점),w(거리))
                cost = dis + i[1]
                if cost < distance[i[0]] :
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
dijkstra(K)
for i in range(1,V+1):
    if distance[i] == inf:
        print('INF')
    else :
        print(distance[i])
