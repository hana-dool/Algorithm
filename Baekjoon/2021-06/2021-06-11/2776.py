T = int(input())
for _ in range(T):
    N = int(input())
    lst1 = set(map(int, input().split()))
    M = int(input())
    lst2 = list(map(int, input().split()))
    dic = {}
    for i in lst1 :
        dic[i] = 1
    for j in lst2 :
        print(dic.get(j,0))

