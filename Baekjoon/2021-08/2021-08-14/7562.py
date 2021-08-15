import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [-2,2,1,-1,2,-2,1,-1]


for _ in range(T) :
    l = int(input())
    # make matrix
    mat = [[0]*l for _ in range(l)]

    now_x,now_y = map(int,input().split())
    mat[now_x][now_y]  = 1
    mx,my = map(int,input().split())

    q = deque([(now_x,now_y,0)])
    while q :
        x,y,cnt = q.popleft()
        if x == mx and y == my :
            print(cnt)
            break
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l :
                if mat[nx][ny] == 0 :
                    mat[nx][ny] = 1
                    q.append((nx,ny,cnt+1))
