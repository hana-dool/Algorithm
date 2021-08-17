import sys
import heapq
inf = 10** 12
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [inf] * (N+1)
for _ in range(M) :
    start, end , price = map(int,input().split())
    graph[start].append((end,price))

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q :
        cost , now = heapq.heappop(q)
        if distance[now] < cost :
            continue
        else :
            for i in graph[now] :
                if distance[i[0]] > i[1] + cost : # 가치있음
                    distance[i[0]] = i[1] + cost
                    heapq.heappush(q,(i[1] + cost,i[0]))
A,B = map(int,input().split())
dijkstra(A)
print(distance[B])