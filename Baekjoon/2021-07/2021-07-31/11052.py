import sys
N = int(input())
lst = list(map(int,input().split()))
lst = [0] + lst
dp = [0]*(N+1)
dp[0] = 0
dp[1] = lst[1]
for i in range(1,N+1) :
    ans = []
    for j in range(1,i+1):
        ans.append(dp[i-j] + lst[j])
    dp[i] = max(ans)
print(dp[-1])
