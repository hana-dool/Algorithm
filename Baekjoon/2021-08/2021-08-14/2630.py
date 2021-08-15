import sys
input = sys.stdin.readline
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]

blue = 0
red = 0
def recur(l,a,b) :
    global blue
    global red
    cnt = 0
    for i in range(a,a+l) :
        for j in range(b,b+l):
            if mat[i][j] == 1 :
                cnt += 1
    if cnt == l*l  :
        blue += 1
        return
    elif cnt == 0 :
        red += 1
        return
    else :
        recur(l//2,a,b)
        recur(l//2,a+l//2,b)
        recur(l//2,a,b+l//2)
        recur(l//2,a+l//2,b+l//2)
recur(N,0,0)
print(red)
print(blue)