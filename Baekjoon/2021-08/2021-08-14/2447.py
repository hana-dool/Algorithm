import sys
input = sys.stdin.readline
N = int(input())
mat = [['*']*N for _ in range(N)]


def recur(x,a,b) :
    if x == 1 :
        return
    l = x // 3
    for i in range(a+l,a+l*2) :
        for j in range(b+l,b+l*2) :
            mat[i][j] = ' '
    for x in range(3):
        for y in range(3) :
            recur(l,x*l+a,y*l+b)

recur(N,0,0)
for i in mat:
    for j in i :
        print(j,end='')
    print()
