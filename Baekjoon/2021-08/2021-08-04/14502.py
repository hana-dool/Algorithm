import sys
from itertools import combinations
import copy
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]

wall = []
for x in range(N):
    for y in range(M):
        if mat[x][y] == 0 :
            wall.append((x,y))

nums = list(combinations(wall,3))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
ans = []
for i in nums :
    mat2 = copy.deepcopy(mat)
    mat2[i[0][0]][i[0][1]] = 1
    mat2[i[1][0]][i[1][1]] = 1
    mat2[i[2][0]][i[2][1]] = 1
    q = deque()
    for i in range(N):
        for j in range(M) :
            if mat2[i][j] == 2 :
                q.append((i,j))
    while q :
        x ,y = q.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx< N and 0<=ny<M:
                if mat2[nx][ny] == 0 :
                    mat2[nx][ny] = 1
                    q.append((nx,ny))
    cnt_0 =0
    for i in mat2 :
        cnt_0 += i.count(0)
    ans.append(cnt_0)
print(max(ans))