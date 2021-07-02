n,m = map(int,input().strip().split())
mat = [list(map(int,list(str(input())))) for _ in range(n)]


# 이는 '직사각형'
mx = 0
def ch_sqr(x,y):
    ans = [1]
    for i in range(1,n):
        for j in range(1,m) :
            if 0<= x+i < n and 0 <= y+j < m :
                if mat[x][y] == mat[x+i][y] == mat[x][y+j] == mat[x+i][y+j] :
                    ans.append((i+1)*(j+1))
    return(max(ans))

val = []
for i in range(n):
    for j in range(m):
        val.append(ch_sqr(i,j))
print(max(val))