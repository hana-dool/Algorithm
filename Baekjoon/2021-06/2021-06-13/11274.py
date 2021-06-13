import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

A,B = map(int,read().split())
r = [ [] for _ in range(A+1) ]
ch = [0]*(A+1)

for _ in range(B):
    x,y = map(int,read().split())
    r[x].append(y)
    r[y].append(x)

# 시작점이 정해졌을때에, DFS
def DFS(i):
    ch[i] = 1
    for j in r[i]:
        if ch[j] == 0 :
            DFS(j)
cnt = 0
for i in range(1,A+1):
    if ch[i] == 0 :
        cnt += 1
        DFS(i)
print(cnt)

