n,m = map(int,input().split())
# m 은 길이가 m 인 수열
# 자연수 n 개에서 m 개를 골라야함

visit = [0]*(n+1)
ans = []
ch = []
def dfs(depth):
    if depth == m :
        print(*ans)
        return
    else :
        for i in range(1,n+1):
            if visit[i] == 0 :
                for j in range(i+1):
                    visit[j] = 1
                ans.append(i)
                dfs(depth+1)
                ans.pop()
                for j in range(i+1):
                    visit[j] = 0
dfs(0)