import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
sin =[]
ssn = []
for _ in range(N):
    a,b = map(int,input().split())
    sin.append(a)
    ssn.append(b)

ans = []
def dfs(s,ss,cnt,all):
    if cnt == N:
        if all[0] >= 1 and all[1] >= 1 :
            ans.append(abs(s-ss))
            return
        else :
            return
    else :
        dfs(s * sin[cnt], ss+ssn[cnt], cnt+1,[all[0]+1,all[1]+1])
        dfs(s, ss , cnt + 1,[all[0],all[1]])
dfs(1,0,0,[0,0])
# 0 일때 어떻게 되려나... ?
print(min(ans))
