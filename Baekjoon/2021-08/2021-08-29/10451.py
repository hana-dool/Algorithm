import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
T = int(input())
for _ in range(T) :
    N = int(input())
    visited = [0]*(N+1)
    cycle = [0] + list(map(int,input().split()))

    def dfs(x) :
        # 이미 visited 가 아닌 수열로 접어들었다고 판단.
        visited[x] = 1
        if visited[cycle[x]] == 0 :
            dfs(cycle[x])
    cnt = 0
    for i in range(1,N+1) :
        if visited[i] == 0 :
            dfs(i)
            cnt += 1
    print(cnt)