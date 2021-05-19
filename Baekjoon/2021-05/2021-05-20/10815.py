import sys
read = sys.stdin.readline

N = int(read())
lst1 = list(map(int,read().split()))
M = int(read())
lst2 = list(map(int,read().split()))

lst1.sort()

stk = []
l = len(lst1)-1
for i in lst2 :
    end = l
    start = 0
    j=0
    while start <= end :
        mid = (start + end)//2
        if lst1[mid] == i :
            stk.append(1)
            j = 1
            break
        elif lst1[mid] > i : # 지금 목표치보다 큼
            end = mid - 1
        elif lst1[mid] < i : # 목표치보다 작음
            start = mid + 1
    if j == 0 :
        stk.append(0)

print(' '.join(list(map(str,stk))))
