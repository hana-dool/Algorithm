T = int(input())
for _ in range(T):
    n = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))

    price = []
    for i in range(len(x)):
        price.append([x[i],y[i]])

    dp = [[0,0] for _ in range(n)]
    dp[0] = price[0]
    if n == 1 :
        print(max(dp[-1]))
        break
    dp[1][0] = (price[0][1] + price[1][0])
    dp[1][1] = (price[0][0] + price[1][1])
    for i in range(2,n):
        dp[i][0] = max(dp[i-1][1]+price[i][0], +dp[i-2][1]+price[i][0])
        dp[i][1] = max(dp[i-1][0]+price[i][1], +dp[i-2][0]+price[i][1])
    print(max(dp[-1]))