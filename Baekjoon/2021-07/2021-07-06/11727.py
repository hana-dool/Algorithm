# 점화식은 다음과 같다.
# a_i = a_{i-1} + a_{i-2}

n = int(input())
dp = [0]*(n+1)

dp[1] = 1
dp[2] = 3
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2
print(dp[-1] % 10007)
