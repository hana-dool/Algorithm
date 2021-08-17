import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
inf = 10**9

mat = [[inf] * (N+1) for _ in range(N+1)]
for i in range(N+1) :
    mat[i][i] = 0

for _ in range(M):
    start,end,price = map(int,input().split())
    mat[start][end] = min( mat[start][end],price)

for mid in range(1,N+1) :
    for i in range(1,N+1) :
        for j in range(1,N+1) :
            mat[i][j] = min(mat[i][j], mat[i][mid] + mat[mid][j])
for i in range(1,N+1) :
    for j in range(1,N+1) :
        if mat[i][j] == 10**9 :
            mat[i][j] = 0

for i in range(1,N+1) :
    print(*mat[i][1:])
