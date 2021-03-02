# https://www.acmicpc.net/problem/9095
import sys
read = sys.stdin.readline

T = int(read())
lis = [0,1,2,4]


mx = 3
for _ in range(T):
    n = int(read())
    if mx >= n :
        print(lis[n])
    else :
        for idx in range(mx+1,n+1): # 3~n
            lis.append(sum(lis[-3:]))
        mx = n
        print(lis[n])







# 점화식으로 정의해야할거같다.
# 1 2
# 2 1
# 3



