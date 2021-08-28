import sys
from collections import defaultdict
input = sys.stdin.readline
K, L = map(int,input().strip().split())

lst = []
dic = defaultdict(int)
for order in range(L) :
    num = input().strip()
    dic[num] = max(dic[num],order)
dic = dict(dic)
ans = sorted(dic.items(),key = lambda x : x[1])
ans_lst = list(map(lambda x : x[0] , ans))
for i in range(min(K,len(ans_lst))) :
    print(ans_lst[i])