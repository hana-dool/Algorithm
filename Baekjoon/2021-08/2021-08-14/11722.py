import sys
input = sys.stdin.readline

A = int(input())
lst = list(map(int,input().split()))
dp = [1]*A
for end in range(A) :
    for search in range(end) :
        if lst[search] > lst[end] :
            dp[end] = max(dp[end], dp[search] + 1 )
print(max(dp))
