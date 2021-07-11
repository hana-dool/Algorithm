import sys
input = sys.stdin.readline
n,m = map(int,input().split())

visit = [0] * (n+1)
ans = []

def dfs(depth):
    if depth == m :
        print(*ans)
        return
    else :
        for i in range(1,n+1):
            ans.append(i)
            dfs(depth+1)
            ans.pop()
dfs(0)