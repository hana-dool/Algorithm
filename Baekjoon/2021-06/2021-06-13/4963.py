import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,0,1,-1,0,1,-1]

def dfs(x,y):
    global cnt
    if ch[y][x] == 0 and mat[y][x] == 1 :
        cnt += 1
        ch[y][x] = 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h :
                if ch[ny][nx] == 0 and mat[ny][nx] == 1 :
                    dfs(nx,ny)

while True :
    w,h = map(int,read().split())
    if (w,h) == (0,0):
        break
    mat = [list(map(int,read().split())) for _ in range(h)]
    ch = [[0]*w for _ in range(h)]
    ans = []
    for i in range(h): # row
        for j in range(w): # col
            cnt = 0
            dfs(j,i)
            ans.append(cnt)
    print(sum([1 for i in ans if i > 0]))


