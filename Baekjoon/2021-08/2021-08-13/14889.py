import sys
input = sys.stdin.readline
N = int(input())
from itertools import combinations
people = list(range(1,N+1))
l = N//2
comb = list(combinations(people,l))
mat = [list(map(int,input().split())) for _ in range(N)]

tot = 0
for row in mat :
    tot += sum(row)

ans = []

cnt = 0
for j in comb :
    comb2 = list(combinations(list(j),2))
    cnt = 0
    cnt2 = 0

    for k in comb2 :
        x,y = k
        cnt += mat[x-1][y-1]
        cnt += mat[y-1][x-1]
    lst = list(range(1,N+1))
    for v in j :
        lst.remove(v)

    comb3 = list(combinations(lst, 2))
    for k in comb3 :
        x,y = k
        cnt2 += mat[x-1][y-1]
        cnt2 += mat[y-1][x-1]
    ans.append(abs(cnt-cnt2))
print(min(ans))


