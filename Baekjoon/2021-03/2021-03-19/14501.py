#https://www.acmicpc.net/problem/14501
# 이거 코드 리뷰 좀 해봐야될듯. dp 를 쓴거는 처음이라 너무 얼렁뚱땅한거같음!!!
import sys
read = sys.stdin.readline
N = int(read())
Time = []
Money = []
for _ in range(N):
    a,b = map(int,read().split())
    Time.append(a)
    Money.append(b)
# 시간과 돈에 관한 리스트를 만든다.
# DP 를 사용하자.
# Memorizing은 그 날 퇴사를 결심하였을 떄, 얻는 최대수익들
# N+1 로 놓은 이유는, indexing error 떄문에
dp = [0]*(N+1)

# dp = [0,0,0,0....0]
# Time 의 index 는 0 ~ N-1
# Monry index 는 0 ~ N-1
# dp 의 index 는 0 ~ N-1

# EX)
# T = [1,1,1,2,2,1,2,3]
# i = [0,1,2,3,4,5,6,7]
# dp= [0,0,0,0,0,0,0,0,0]
# N = 8 인 상황

for i in range(N-1,-1,-1): # N-1 .... 0
    if i == N-1 :
        if Time[i]+i <= N :
            dp[i] = Money[i]
    elif Time[i]+i <= N :
        dp[i] = max(dp[i+Time[i]]+Money[i],dp[i+1])
    else :
        dp[i] = dp[i+1]
print(dp[0])





