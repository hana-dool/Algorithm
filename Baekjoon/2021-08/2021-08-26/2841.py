import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline
N,P = map(int,input().split())
dic = defaultdict(list)

for _ in range(N) :
    number,pret = map(int,input().split())
    dic[number].append(pret)
dic = dict(dic)
# [8,10,12,10,5]
#
def cnt_move(lst) :


cnt = 0
for lst in dic.values() :
    cnt += cnt_move(lst)
print(cnt)