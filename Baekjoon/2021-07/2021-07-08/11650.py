n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
s_lst = sorted(lst,key= lambda x : (x[0],x[1]))
for i in s_lst :
    a,b = i
    print(a,end =' ')
    print(b)
