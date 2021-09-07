N = int(input())
lst = list(map(int,input().split()))
lst.sort()
target = int(input())
inf = 10**9
dp = [inf] * (target+1)
dp[0] = 0

for price in lst :
    for i in range(target+1) :
        if i-price >=0 :
            dp[i] = min(dp[i],dp[i-price]+1)
print(dp[-1])