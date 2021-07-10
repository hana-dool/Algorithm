n,m = map(int,input().split())
lst = list(map(int,input().split()))
length = len(lst)
cnt = 0
s = 0 # start points
e = 1 # ends points
while True :
    if e > n :
        break
    else :
        if sum(lst[s:e]) == m :
            cnt += 1
            s += 1
        elif sum(lst[s:e]) > m :
            s += 1
        else :
            e += 1
print(cnt)