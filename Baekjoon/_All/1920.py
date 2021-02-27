import sys
read = sys.stdin.readline

N = int(read())
lis = list(map(int,read().split()))
M = int(read())
lis2 = list(map(int,read().split()))

lis.sort()
# 아래 식으로 대충 in 함수로 하게 되면 시간 초과가 일어난다.
# 그러므로 Binary search 를 진행해야 한다.
# for val in lis2:
#     if val in lis :
#         print(1)
#     else :
#         print(0)
for val in lis2 :
    l = 0
    r = N-1
    while True :
        mid = (l + r)//2
        if (l == r) and val != lis[mid] :
            print(0)
            break
        if val == lis[mid]:
            print(1)
            break
        elif val > lis[mid]:
            l = mid+1
        else :
            r = mid
