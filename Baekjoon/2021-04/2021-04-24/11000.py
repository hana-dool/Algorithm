# https://www.acmicpc.net/problem/11000

import sys
read = sys.stdin.readline

N = int(read())

lst = [tuple(map(int,read().split())) for _ in range(N)]
lst.sort(key = lambda x : (x[0],x[1])) # 첫번째 기준 정렬하다가 두번쨰 값 기준으로 정렬



# 아래는 시간초과로 인해서 폐기된 풀이입니다.
# while lst :
#     cls = lst.pop(0)
#     late = lst[-1][0] # 가장 늦게 시작하는 강의
#     for i in lst :
#         if i[1] > late :
#             lst.remove(i) # 가장 늦게 시작하는 강의보다 더 늦으면 안됨..
#             break
#         elif cls[1] <= i[0] :
#              cls = i
#              lst.remove(i)
#     cnt += 1
# print(cnt)


# List 로 풀게되면 시간복잡도로 인해, 시간초과를 겪게 됩니다.
# 그러므로 heapq 로 풀어야 합니다.
import heapq as hp
q = []
hp.heappush(q,lst[0][1]) # 처음 강의의 끝나는 시간
# heapq 의 장점은 '실시간으로 계속 정렬된다' 라는것입니다.
# 즉 q[0] 은 업데이트를 계속 함에도 불구하고, 제일 작은값이 딥니다.
# 이떄에, 정렬을 시켰기 떄문에, 최대한 공강이 없게 짤 수 있습니다.
for i in range(1,N):
    if q[0] > lst[i][0]: # 끝나는 시간 > 시작하는 시간 이면 불가능
        hp.heappush(q,lst[i][1]) # 그러면 그냥 넣기
    else: # 그렇지 않으면, 끝나는 시간 <= 시작하는 시간 즉 연강 가능
        hp.heappop(q)
        hp.heappush(q,lst[i][1])
print(len(q))

