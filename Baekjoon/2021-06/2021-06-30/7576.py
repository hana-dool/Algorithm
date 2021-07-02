m,n = map(int,input().strip().split())
mat = [list(map(int,input().strip().split())) for _ in range(n)]

from collections import deque
queue = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    for j in range(m):
        if mat[i][j] not in (0,-1) :
            queue.append((i,j))
while queue:
    x,y = queue.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m :
            if mat[nx][ny] == 0:
                mat[nx][ny] = mat[x][y] + 1
                queue.append((nx,ny))
mx = 0
kk = 0
for i in mat :
    if 0 in i :
        kk = 1
        break
    if max(i) > mx :
        mx = max(i)
if kk == 1 :
    print(-1)
else :
    print(mx-1)