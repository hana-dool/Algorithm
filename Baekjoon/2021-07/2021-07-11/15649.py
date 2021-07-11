n,m = map(int,input().split())
# 1~n 까지의 자연수 중에서 중복없이 M 개를고른 수열
visit = [0] * (n+1)
ans = []
def dfs(depth):
    if depth == m : # 조건부
        print(*ans) # 출력부
        return
    else :
        for i in range(1,n+1): # 조건부
            if visit[i] == 0 :
                visit[i] = 1
                ans.append(i)
                dfs(depth+1) # 재귀부
                visit[i] = 0 # 원상 복귀부
                ans.pop()
dfs(0)