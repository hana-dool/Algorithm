import sys
import heapq

input = sys.stdin.readline
T  = int(input())
for _ in range(T) :
    visited = [0]*1000001
    k = int(input())
    min_q = []
    max_q = []
    length = 0
    for _ in range(k) :
        operator,val= input().split()
        if operator == 'I' :
            heapq.heappush(min_q,int(val))
            heapq.heappush(max_q,-1*int(val))
            visited[int(val)] = 1
            length += 1
        elif operator == 'D' :
            if length != 0 :
                if val == '-1' :
                    trash = heapq.heappop(min_q)
                    visited[trash] = 0
                    length -= 1
                else :
                    trash = heapq.heappop(max_q)
                    visited[trash] = 0
                    length -= 1
    if length == 0 :
        print('EMPTY')
    else :
        print(-1*int(min(max_q)),min(min_q))