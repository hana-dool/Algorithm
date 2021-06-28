from collections import deque
N,M = map(int,input().split())
mat = [list(map(int,list(input()))) for _ in range(N)]
ch = [[0]*M for i in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

ch[0][0] = 1
queue = deque()
queue.append((0,0))
while queue :
    x,y = queue.popleft()
    if x == M-1 and y == N-1 :
        print(ch[N-1][M-1])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N :
            if ch[ny][nx] == 0 and mat[ny][nx] == 1:
                queue.append((nx,ny))
                ch[ny][nx] = ch[y][x] + 1


# if nx < 0 or M <= nx or ny < 0 or N <= ny or mat[ny][nx] == 0 or ch[ny][nx] >= 1:
#     continue
# else:
#     queue.append((nx, ny))
#     ch[ny][nx] = ch[y][x] + 1
#