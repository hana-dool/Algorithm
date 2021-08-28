import sys
input = sys.stdin.readline
N,M = map(int,input().split())
mat_raw = [list(map(int,list(input().strip()))) for _ in range(N)]
mat_wt = [list(map(int,list(input().strip()))) for _ in range(N)]

def change_3x3(x,y,mat) :
    for i in range(3) :
        for j in range(3) :
            mat[x+i][y+j] = abs(mat[x+i][y+j]-1)
    return mat
cnt = 0
for x in range(N-2) :
    for y in range(M-2) :
        if mat_raw[x][y] != mat_wt[x][y] :
            mat_raw = change_3x3(x,y,mat_raw)
            cnt += 1
if mat_raw == mat_wt :
    print(cnt)
else :
    print(-1)

for x in range(0) :
    print(x)