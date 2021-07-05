# dp 방법으로 재풀이 입니다.
# 원래는 bfs

n = int(input())
dp = [ 0 for _ in range(n+1)]

for i in range(2,n+1):
    lst = []
    if i > 0 :
        lst.append(dp[i-1])
    if i % 2 == 0 :
        lst.append(dp[i//2])
    if i % 3 == 0 :
        lst.append(dp[i//3])
    dp[i] = min(lst) + 1
print(dp[-1])