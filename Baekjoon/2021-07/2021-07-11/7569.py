import sys
input = sys.stdin.readline

m,n,h = map(int,input().split())
cubic = []
for height in range(h):
    mat = [list(map(int,input().split())) for i in range(n)]
    cubic.append(mat)

from collections import deque
q = deque([])
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

for H in range(h):
    for N in range(n):
        for M in range(m):
            if cubic[H][N][M] == 1:
                q.append((H,N,M))

while q  :
    H,N,M = q.popleft()
    for i in range(6):
        nH = H + dx[i]
        nN = N + dy[i]
        nM = M + dz[i]
        if 0 <= nH < h and 0 <= nN < n and 0 <= nM < m :
            if cubic[nH][nN][nM] == 0 :
                cubic[nH][nN][nM] = cubic[H][N][M] + 1
                q.append((nH,nN,nM))

# 0 이 있는지 체크
mx = 0
for H in range(h):
    for N in range(n):
        for M in range(m):
            if cubic[H][N][M] == 0 :
                print(-1)
                sys.exit(0)
            else :
                if mx < cubic[H][N][M] :
                    mx = cubic[H][N][M]
print(mx-1)
# 0 이 없다면
