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
            print(heapq.heappop(heap))
    else :
        heapq.heappush(heap,v)

