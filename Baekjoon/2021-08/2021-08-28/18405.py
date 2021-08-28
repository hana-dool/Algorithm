import sys
from collections import deque
input  = sys.stdin.readline
N,K = map(int,input().split())
mat= [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())

q = deque()
for look in range(1, K + 1):
    for i in range(N) :
        for j in range(N) :
            if mat[i][j] == look :
                q.append((mat[i][j],i,j,0))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
check = 0
while q :
    val, x, y, cnt = q.popleft()
    # S 초일떄에는 그만깊어지기
    if x == X-1 and y == Y-1 :
        check = 1
        print(val)
        break
    if cnt < S :
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny < N  :
                if mat[nx][ny] == 0 :
                    mat[nx][ny] = val
                    q.append((val,nx,ny,cnt+1))
if check == 0 :
    print(0)