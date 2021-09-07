import sys
import heapq

input = sys.stdin.readline
T  = int(input())
visited = [0]*1000001
for _ in range(T) :
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
                    while True :
                        check = heapq.heappop(min_q)
                        if visited[check] == 1 :
                            visited[check] = 0
                            length -= 1
                            break
                else :
                    while True :
                        check = heapq.heappop(max_q)
                        if visited[-1*check] == 1 :
                            visited[-1*check] = 0
                            length -= 1
                            break
    if length == 0 :
        print('EMPTY')
    else :
        ans = []
        for i in range(1000001) :
            if visited[i] == 1 :
                ans.append(i)
        print(max(ans),min(ans))
