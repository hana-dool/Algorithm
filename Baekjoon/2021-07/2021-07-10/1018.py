import sys
input = sys.stdin.readline

n,m = map(int,input().split())
mat = []
mat = [list(input().strip()) for _ in range(n)]
window_1 = [['W','B']*4,['B','W']*4]*4
window_2 = [['B','W']*4,['W','B']*4]*4
ans = []
for i in range(n):
    for j in range(m):
        if i+8 <= n and j+8 <= m :
            val1,val2 = 0,0
            for x in range(8):
                for y in range(8):
                    if mat[i+x][j+y] != window_1[x][y] :
                        val1 += 1
                    if mat[i+x][j+y] != window_2[x][y] :
                        val2 += 1
            ans.extend([val1,val2])
print(min(ans))