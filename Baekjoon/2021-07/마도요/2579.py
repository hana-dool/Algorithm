import sys
dp = [0] * 301
n = int(input())
score = [int(input()) for _ in range(n)]
if n == 1 :
    print(score[0])
    sys.exit(0)
if n == 2 :
    print(score[0] + score[1])
    sys.exit(0)
if n == 3 :
    print(max(score[1] + score[2], score[2]+score[0]))
    sys.exit(0)
dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[1] + score[2], score[2]+score[0])
for i in range(3,n):
    dp[i] = max(score[i] + dp[i-2] , score[i] +score[i-1]+ dp[i-3])
print(dp[n-1])