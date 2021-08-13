# N = 1000
# 상당히 적은편

N = int(input())
# dp 를 하는데 , 경우의 수를 나누는 테크닉인듯 .
dp = [[] for _ in range(N)]
dp[0] = [1,1,1,1,1,1,1,1,1,1] # 0 ~ 9 로 끝나는 수들의 모음

for i in range(1,N):
    for k in range(10) :
        val = 0
        for j in range(k+1) :
            val += dp[i-1][j]
        dp[i].append(val)
print(sum(dp[-1]) % 10007)


# 1 2 3 4 5 6 7 8 9 0
# 11