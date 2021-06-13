import sys
read = sys.stdin.readline

row , col = map(int,read().split())
mat = []
for i in range(row):
    mat.append(list(read().strip())+['o'])
mat.append(['o']*(col+1))

cnt = 0
for i in range(row):
    for j in range(col):
        if mat[i][j] == '|' :
            continue
        elif mat[i][j+1] == '-' :
            continue
        else :
            cnt += 1

for i in range(col):
    for j in range(row):
        if mat[j][i] == '-':
            continue
        elif mat[j+1][i] == '|' :
            continue
        else :
            cnt += 1

print(cnt)
