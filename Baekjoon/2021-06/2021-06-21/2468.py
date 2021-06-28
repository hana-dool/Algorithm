import sys
read = sys.stdin.readline
sys.setrecursionlimit(1000000000)

N = int(read())

mat = [list(map(int,read().strip().split()))for _ in range(N)]

mx = 0
for i in range(N):
    for j in range(N) :
        if mx < mat[i][j] :
            mx = mat[i][j]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 위치가 주어졌을때, 그 주변을 탐색하며서 잠길지 아닐지 결정한다.
cnt = 0
# 우선 들어가기만 하면,
def dfs(x,y,v) :
    global cnt
    if ch[y][x] == 0 and mat[y][x] > v:
        cnt += 1
        ch[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0<= ny < N :
                dfs(nx,ny,v)

val = []
for v in range(mx):
    ans = []
    ch = [[0] * N for _ in range(N)]
    for i in range(N) :
        for j in range(N):
            cnt = 0
            dfs(i,j,v)
            if cnt != 0:
                ans.append(cnt)
    val.append(len(ans))
print(max(val))
