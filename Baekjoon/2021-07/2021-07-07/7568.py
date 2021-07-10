n = int(input())
size = [tuple(map(int,input().split())) for _ in range(n)]
lst = [1] * n

for v,i in enumerate(size) :
    for j in size :
        if j[0] > i[0] and j[1] > i[1] :
            lst[v] += 1

for i in lst:
    print(i , end =' ')
