N = int(input())
dic = {}
for _ in range(N):
    a,b = input().split()
    dic[a] = int(b)

lst = sorted(dic.items(),key = lambda x : x[1])
for i,v in lst :
    print(i,end = ' ')