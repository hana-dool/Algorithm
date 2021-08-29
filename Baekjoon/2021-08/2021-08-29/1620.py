import sys
from collections import defaultdict
input = sys.stdin.readline
N , M = map(int,input().split())
lst = [input().strip() for _ in range(N)]
dic_key_idx = dict()
dic_key_name = dict()
for idx , val in enumerate(lst) :
    dic_key_idx[str(idx+1)] = val
    dic_key_name[val] = str(idx+1)


for _ in range(M) :
    problem = input().strip()
    if problem.isdigit() :
        print(dic_key_idx[problem])
    else :
        print(dic_key_name[problem])

