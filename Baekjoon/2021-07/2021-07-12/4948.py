import math
dp = [0,1,1] + [0]*250000
def ch(x):
    for i in range(2,int(math.sqrt(x))+1) :
        if x % i == 0 :
            return(0) # 합성수일떄
    return(1) # 소수일떄
for i in range(250000):
    dp[i] = ch(i)
while True :
    val = int(input())
    if val == 0 :
        break
    ans = sum(dp[val+1:2*val+1])
    print(ans)