import sys
input = sys.stdin.readline
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]

# x,y, 는 왼쪽 시작점
# l 은 돌아가는 순회지점.
dic = {-1:0,0:0,1:0}
def recursion(x,y,l):
    val = mat[x][y]
    for i in range(l) :
        for j in range(l) :
            if mat[x+i][y+j] != val : # 아니면.. 깊어지기
                l = l//3
                for k in range(3):
                    for g in range(3):
                        recursion(x+l*k,y+l*g,l)
                return
    dic[val] += 1
recursion(0,0,len(mat))
for i in dic.values():
    print(i)