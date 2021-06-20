import sys
read = sys.stdin.readline
N = int(read().strip())
lst = list(map(int,read().strip().split(' ')))
dic = {}
for idx,v in enumerate(lst):
    dic[idx] = v

ans = sorted(dic.items(),key = lambda x : (x[1],x[0]))
print(ans)
for i in ans :
    print (i[0], end = ' ')
