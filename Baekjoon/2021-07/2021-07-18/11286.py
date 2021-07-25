import heapq
import sys
input = sys.stdin.readline
N = int(input())

q = []

for _ in range(N):
    x = int(input())
    if x == 0 :
        if q :
            element = heapq.heappop(q)
            print(element[1])
        else :
            print(0)
    else :
        heapq.heappush(q,(abs(x),x))


sum([])


min([(2, 0), (1, 1), (3, 2), (2, 3)],key = lambda x :x[1])