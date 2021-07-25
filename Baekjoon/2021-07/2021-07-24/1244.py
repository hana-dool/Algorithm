import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
T = int(input())
for _ in range(T):
    sex,num = map(int,input().split())
    if sex == 2 : # 여학생
        mid = num - 1
        start = mid
        end = mid
        while start >= 0 and end < n:
            if lst[start] == lst[end] :
                lst[start] = lst[end] = abs(lst[start] - 1)
                start = start - 1
                end = end + 1
            else :
                break
    else : # 남학생
        i = 1
        while i * num  <= n  :
            lst[i*num-1] = abs(lst[i*num-1] - 1 )
            i += 1
idx = 1
while idx <= n :
    if idx % 20 != 0 :
        print(lst[idx-1], end = ' ')
        idx = idx + 1
    else :
        print(lst[idx-1])
        idx = idx + 1
