import sys
read = sys.stdin.readline

from sys import*
setrecursionlimit(1000000)

m,n,k = map(int,read().split())


mat = [[0]*n for _ in range(m)]
ch = [[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,read().split())
    for i in range(min(x1,x2),max(x1,x2)):
        for j in range(min(y1,y2),max(y1,y2)):
            mat[j][i] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

from collections import deque
queue = deque()


# m 은 세로
# n 은 가로
ans = []
for i in range(n):
    for j in range(m):
        if mat[j][i] == 0 :
            cnt = 1
            mat[j][i] = 1
            queue.append((i, j))
            while queue :
                x,y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m :
                        if mat[ny][nx] == 0 :
                            queue.append((nx,ny))
                            mat[ny][nx] = 1
                            cnt += 1
            ans.append(cnt)
ans.sort()
print(len(ans))
for i in ans :
    print(i, end=' ')










# def dfs(x,y):
#     global cnt
#     mat[y][x] = 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m :
#             if mat[ny][nx] == 0 :
#                 cnt += 1
#                 dfs(nx,ny)
# ans = []
# for x in range(n) :
#     for y in range(m):
#         if mat[y][x] == 0 :
#             cnt = 1
#             dfs(x,y)
#             ans.append(cnt)
# ans.sort()
#
# print(len(ans))
# for i in ans :
#     if i == max(ans):
#         print(i, end = '')
#     else :
#         print(i, end = ' ')
#
