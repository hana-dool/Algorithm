import sys
import heapq

input = sys.stdin.readline
T  = int(input())
visited = [0]*10
for _ in range(T) :
    k = int(input())
    min_q = []
    max_q = []
    length = 0
    for _ in range(k) :
        operator,val= input().split()
        if operator == 'I' :
            heapq.heappush(min_q,(int(val),_))
            heapq.heappush(max_q,(-1*int(val),_))
            length += 1
        elif operator == 'D' :
            if length != 0 :
                if val == '-1' :
                    while True :
                        pop_val = heapq.heappop(min_q)
                        if not pop_val :
                            break
                        if visited[pop_val[1]] == 0 :
                            visited[pop_val[1]] = 1
                            break
                else :
                    while True :
                        print(pop_val)
                        pop_val = heapq.heappop(max_q)
                        if not pop_val :
                            break
                        if visited[pop_val[1]] == 0 :
                            visited[pop_val[1]] = 1
                            break
    if length == 0 :
        print('EMPTY')
    else :
        print(-1*max_q[0][0] , min_q[0][0])
