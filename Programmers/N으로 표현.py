# 음...

def solution(N, number):
    dp = [[] for _ in range(9)]
    dp[1] = [N]
    dp[2] = [N*N, N//N , N+N, N-N , int(str(N)+str(N))]
    for i in range(3,9):
        for j in range(i):
            dp[i] = dp[i-1] + dp[1]

    answer = 0
    return answer


i = [2,3,4]
all(i[l]>2 for l in range(3))