import sys
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
dp = [0]*n
if n == 1 :
    print(lst[0])
    sys.exit(0)
if n == 2 :
    print(lst[0]+lst[1])
    sys.exit(0)
dp[0] = lst[0]
dp[1] = lst[0]+lst[1]
dp[2] = max(lst[0]+lst[1],lst[2]+lst[1],lst[0]+lst[2])
for i in range(3,n):
    dp[i] = max(dp[i-1],dp[i-2]+lst[i],dp[i-3]+lst[i]+lst[i-1])
print(dp[-1])