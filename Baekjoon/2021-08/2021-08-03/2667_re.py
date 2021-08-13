import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
mat = [list(map(int,list(input().strip()))) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b) :
    q = deque([(a,b)])
    cnt = 1
    mat[a][b] = 0
    while q :
        x,y= q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N :
                if mat[nx][ny] == 1 :
                    mat[nx][ny] = 0
                    q.append((nx,ny))
                    cnt += 1
    return cnt
ans = []
for i in range(N) :
    for j in range(N) :
        if mat[i][j] == 1 :
            cnt = bfs(i,j)
            ans.append(cnt)
ans.sort()
print(len(ans))
for i in ans :
    print(i)