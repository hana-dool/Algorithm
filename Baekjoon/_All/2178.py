
# 우선 경로탐색이니까... BFS 느낌?

import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = [list(map(int,list(read().strip()))) for _ in range(N)]
num = [[0]*M for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# BFS
path = [(0,0)] # tuple 을 써야 메모리 절약이 조금이라도 더됨
num[0][0] = 1 # 1 을 통해서 얼마나 걸렸는지 표시

while path:
    x, y = path.pop(0) # 맨 앞의 경로를 꺼낸다.

    if x == N-1 and y == M-1:
        print(num[x][y])
        break

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < M: # 경로가 우리 mat 안에 잘 들어와있고
            if mat[xx][yy] == 1 and num[xx][yy] == 0 :
                # 추가적으로 갈 곳이 0 으로 되어있다면
                num[xx][yy] = num[x][y] + 1
                path.append((xx,yy))
