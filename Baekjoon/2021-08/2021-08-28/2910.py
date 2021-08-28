import sys
input = sys.stdin.readline

N,C = map(int,input().split())

lst = list(map(int,input().split()))

dic = dict()
for idx, val in enumerate(lst):
    dic[val] = dic.get(val,[10**9,0])
    dic[val][0] = min(dic[val][0],idx)
    dic[val][1] = dic[val][1] + 1
ans = sorted(dic.items(), key = lambda x : (x[1][1],-x[1][0]), reverse = True )

rst = []
for tup in ans :
    rst.extend([tup[0]]*tup[1][1])
print(*rst)
