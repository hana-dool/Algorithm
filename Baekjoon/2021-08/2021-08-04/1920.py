import bisect
N = int(input())
lst = list(map(int,input().split()))
lst.sort()
M = int(input())
check = list(map(int,input().split()))

for i in check :
    idx = bisect.bisect_left(lst,i)
    if idx >= N :
        print(0)
    elif lst[idx] == i :
        print(1)
    else :
        print(0)