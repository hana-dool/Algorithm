import sys
read = sys.stdin.readline
N = int(read())
lst = list(map(int,read().split()))
M = int(input())

def money(lst,cut):
    sum = 0
    for i in lst:
        if cut < i :
            sum += cut
        else :
            sum += i
    return sum

start = M // N
end = max(lst)

while start <= end :
    mid = (start + end ) //2
    if money(lst,mid) == M :
        start = mid + 1 # 같다고 해도, 더하는것이 핵심.
    elif money(lst,mid) > M : # mid가 너무 큰것.
        end = mid -1
    else : # mid 가 너무 작은것
        start = mid + 1
print(end)


