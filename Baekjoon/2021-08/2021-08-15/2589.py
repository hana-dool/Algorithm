import sys
input = sys.stdin.readline
from collections import deque
import copy

m,n = map(int,input().split())
mat = [list(input()) for _ in range(m)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(i,j,mat2) :
    ans = []
    q = deque([(i,j,0)])
    mat2[i][j] = 0
    while q :
        x,y,cnt = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0 <= ny < n :
                if mat2[nx][ny] == 'L' :
                    mat2[nx][ny] = mat2[x][y]+1
                    q.append((nx,ny,cnt+1))
    return cnt

rst = []
for i in range(m) :
    for j in range(n) :
        if mat[i][j] == "L":
            mat2 = copy.deepcopy(mat)
            rst.append(bfs(i,j,mat2))
print(max(rst))