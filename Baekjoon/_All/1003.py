# https://www.acmicpc.net/problem/1003

import sys
read = sys.stdin.readline

T = int(read())
dic = {0:[1,0],1:[0,1]}

for i in range(2,41):
    dic[i] = [0,0]
    dic[i][0] = dic[i-2][0] + dic[i-1][0]
    dic[i][1] = dic[i-2][1] + dic[i-1][1]

for _ in range(T):
    n = int(read())
    print(dic[n][0],end= ' ')
    print(dic[n][1])

# 딱 보니까 점화식이네
# 그런데 시간제한떄문에 걸릴수도 있겠다.
# 딱 dict 로 구성하면 제맛일거같다.
# 0 -> f(0) = [0,1]
# 1 -> 1 -> f(1) = [1,0]
# 2 -> 1 0 -> f(2) = [1,1]
# 3 -> 1 2 -> f(1) + f(2) = [2,1]
# 4 -> 2 3 -> f(2) + f(3) = [3,2] ....
# 5 -> 3 4 -> 1 2 2 3 -> 1 0 1 0 1 1 2 -> 1 0 1 0 1 1 1 0




#