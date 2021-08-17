import sys
input = sys.stdin.readline

V,E = map(int,input().split())
inf = 10** 9
mat = [[inf] * (V+1) for _ in range(V+1)]

for _ in range(E) :
    start, end , length = map(int,input().split())
    mat[start][end] = length

for mid in range(1,V+1) :
    for i in range(1, V+1) :
        for j in range(1,V+1) :
            mat[i][j] = min(mat[i][j],mat[i][mid] + mat[mid][j])

mn = 10**9
for i in range(1,V+1) :
    mn = min(mn,mat[i][i])
if mn == 10**9 :
    print(-1)
else :
    print(mn)
