import sys
read = sys.stdin.readline

row , col = map(int,read().split())
mat = []
for i in range(row):
    mat.append(list(read().strip()))

cnt = 0
for i in range(row):
    cnt += 1 # 처음에는 무조건 하나 판자 필요
    for j in range(col-1):
        if mat[j] == '-' and mat[j+1] == '-' :
            pass
        else :
            cnt += 1

for i in range(col):
    cnt += 1 # 처음에는 무조건 하나 판자 필요
    for j in range(row-1):
        if mat[j][i] == '|' and mat[j+1][i] == '|' :
            pass
        else :
            cnt += 1
print(cnt)
