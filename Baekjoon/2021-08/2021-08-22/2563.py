import sys
input = sys.stdin.readline

mat = [ [0] * 100 for _ in range(100)]

N = int(input())
for _ in range(N) :
    x,y  = map(int,input().split())
    for i in range(10) :
        for j in range(10) :
            mat[i+y][j+x] = 1
cnt = 0
for row in mat :
    cnt += row.count(1)
print(cnt)