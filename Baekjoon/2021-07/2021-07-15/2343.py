n,m = map(int,input().split())
lst = list(map(int,input().split()))

start = max(lst)
end = sum(lst)

def cal(length) :
    v = 0
    cnt = 0
    for i in lst :
        if v + i > length :
            v = i
            cnt += 1
        else :
            v = v+ i
    cnt += 1
    return cnt

while start <= end :
    mid = (start + end) // 2
    if cal(mid) == m :
        end = mid - 1
    elif cal(mid) < m :
        end = mid - 1
    elif cal(mid) > m :
        start = mid + 1
print(start)