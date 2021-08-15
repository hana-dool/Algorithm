import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[0,0] for _ in range(n)]
    up_lst = list(map(int,input().split()))
    down_lst = list(map(int,input().split()))
    dp[0][0] = up_lst[0]
    dp[0][1] = down_lst[0]
    if n > 1 :
        dp[1][0] = up_lst[1] + dp[0][1]
        dp[1][1] = down_lst[1] + dp[0][0]
        for i in range(2,n) :
            dp[i][0] = max(dp[i-1][1] + up_lst[i], # down up case
                           dp[i-2][0] + up_lst[i],
                           dp[i-2][1] + up_lst[i]) # up non up case
            dp[i][1] = max(dp[i-1][0] + down_lst[i],  # up down case
                           dp[i-2][1] + down_lst[i],
                           dp[i-2][0] + down_lst[i]) # down non down case
    print(max(dp[-1][0],dp[-1][1]))