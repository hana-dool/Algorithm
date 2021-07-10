k = int(input())
lst = []
for _ in range(k):
    j = int(input())
    if j == 0 :
        if len(lst) > 0 :
            lst.pop()
    else :
        lst.append(j)
print(sum(lst))