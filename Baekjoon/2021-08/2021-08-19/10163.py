import sys
input = sys.stdin.readline

N = int(input())
mat = [[' '] *101 for _ in range(101)]

for k in range(N):
    x,y,width,height = map(int,input().split())
    for i in range(x,x+width) :
        for j in range(y,y+height) :
            mat[i][j] = k

ans = [0]*N
for i in range(101):
    for j in range(101):
        if mat[i][j] != ' ':
            ans[mat[i][j]] += 1
for i in ans :
    print(i)