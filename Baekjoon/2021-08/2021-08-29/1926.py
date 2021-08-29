import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i,j):
    # Assume mat[i][j] = 1
    # return cnt 1
    q = deque([])
    q.append((i, j))
    cnt = 1
    mat[i][j] = 0
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx< N and 0<= ny < M :
                if mat[nx][ny] == 1 :
                    mat[nx][ny] = 0
                    q.append((nx,ny))
                    cnt += 1
    return cnt

ans = []
for x in range(N) :
    for y in range(M) :
        if mat[x][y] ==1 :
            val = bfs(x,y)
            ans.append(val)

if not ans :
    print(0)
    print(0)
else :
    print(len(ans))
    print(max(ans))
