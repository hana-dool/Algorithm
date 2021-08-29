import sys
from collections import defaultdict
import heapq
inf = 10**9
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
graph = defaultdict(list)
distance = N * [inf]
distance[0] = 0

for idx, val in enumerate(lst) :
    for i in range(1,val+1) :
        if idx + i < N :
            graph[idx].append((idx+i,1)) # (place , cost)
# set cost 1

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    while q :
        cost , now = heapq.heappop(q)
        if distance[now] < cost :
            continue
        else :
            for i in graph[now] :
                end , price = i
                if cost + price < distance[end] :
                    distance[end] = cost + price
                    heapq.heappush(q,(cost + price , end))
dijkstra(0)
if distance[-1] == inf :
    print(-1)
else :
    print(distance[-1])
