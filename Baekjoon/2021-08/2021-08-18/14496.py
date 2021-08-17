import sys
import heapq
input  = sys.stdin.readline
inf = 10**12

start , end = map(int,input().split())
N , M = map(int,input().split())
distance = [inf] * (N+1)
distance[start] = 0

tree = [[] for _ in range(N+1)]
for _ in range(M) :
    a,b = map(int,input().split())
    tree[a].append([b,1])
    tree[b].append([a,1])

def dijstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    while q :
        cost,now = heapq.heappop(q)
        for i in tree[now] :
            if distance[i[0]] < cost :
                continue
            else :
                if distance[i[0]] > cost + i[1] :
                    distance[i[0]] = cost + i[1]
                    heapq.heappush(q,(cost + i[1],i[0]))
dijstra(start)
if distance[end] == 10**12 :
    print(-1)
else :
    print(distance[end])

print(distance)
