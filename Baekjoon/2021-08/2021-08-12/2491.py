N = int(input())
lst = list(map(int,input().split()))

l = len(lst)
mn = 0
length = 0
ans = []
for i in range(l) :
    if mn <= lst[i] :
        mn = lst[i]
        length += 1
    else :
        mn = lst[i]
        ans.append(length)
        length = 1
ans.append(length)

mx = 0
length = 0
for i in range(l) :
    if mx >= lst[i] :
        mx = lst[i]
        length += 1
    else :
        mx = lst[i]
        ans.append(length)
        length = 1
ans.append(length)
print(max(ans))

