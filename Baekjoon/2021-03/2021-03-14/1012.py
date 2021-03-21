#https://www.acmicpc.net/problem/1012
import sys
read = sys.stdin.readline


dx = [0,0,1,-1]
dy = [1,-1,0,0]

# place 를 받아서, 그와 연결되어있는 배추들을 싸그리 0 으로 만들어버림...

def dfs(place,mat):
    global check
    queue = [place] # 큐로 DFS 구현
    while queue:
        x,y = queue.pop(0)
        mat[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and mat[nx][ny] == 1 and check[nx][ny] == 0 :
                queue.append((nx, ny))
                mat[nx][ny] = 0
                check[nx][ny] = 1


# ------------ 배추를 mat 으로 받는구간 ----------------#
T = int(read())
for _ in range(T): #
    M,N,K = map(int,read().split())
    check = [[0] * M for _ in range(N)]
    mat = [[0]*M for _ in range(N)] # matrix
    for _ in range(K):
        x,y = map(int,read().split())
        mat[y][x] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                check[i][j] = 1
                cnt += 1
                dfs((i, j), mat)
    print(cnt)
