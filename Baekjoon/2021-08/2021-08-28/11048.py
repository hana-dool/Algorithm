import sys
# dp
input = sys.stdin.readline
N,M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
for x in range(1,M) :
    mat[0][x] = mat[0][x-1] + mat[0][x]
for y in range(1,N) :
    mat[y][0] = mat[y-1][0] + mat[y][0]
for x in range(1,N) :
    for y in range(1,M) :
        mat[x][y] = max(mat[x-1][y],mat[x][y-1]) + mat[x][y]
print(mat[-1][-1])