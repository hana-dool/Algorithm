import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N = int(read())
mat = [list(map(int,read().strip())) for _ in range(N)]
ch = [[0]*N for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 갯수를 세주는 recursion 을 정의해야한다.
cnt = 0
def dfs(x,y):
    global cnt
    cnt += 1
    ch[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N :
            if mat[ny][nx] == 1 and ch[ny][nx] == 0 :
                dfs(nx,ny)

ans = []
for x in range(N) : # row
    for y in range(N) : # col
        if ch[y][x] == 0 and mat[y][x] == 1 :
            cnt = 0
            dfs(x,y)
            ans.append(cnt)

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])


