import sys
import heapq
input = sys.stdin. readline

n , m  = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

heapq.heapify(lst)
for _ in range(m) :
    val1 = heapq.heappop(lst)
    val2 = heapq.heappop(lst)
    val1 , val2 = val1+val2 , val1+val2
    heapq.heappush(lst,val1)
    heapq.heappush(lst,val2)
print(sum(lst))