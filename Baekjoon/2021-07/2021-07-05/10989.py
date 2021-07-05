import sys
read = sys.stdin.readline

i = int(read().strip())
dic = {}
for _ in range(i):
    v = int(read().strip())
    dic[v] = dic.get(v,0) + 1

dic = sorted(dic.items(),key = lambda x : x[0])
for i, v in dic :
    for _ in range(v):
        print(i)