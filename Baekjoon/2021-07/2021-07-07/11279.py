import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    v = int(input())
    if v == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            ans = heapq.heappop(heap)
            print(-1 * ans)
    else :
        heapq.heappush(heap,-1*v)