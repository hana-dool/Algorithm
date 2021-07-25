def solution(board):
    m = len(board)  # 세로
    n = len(board[0])  # 가로
    dp = [[0] * n for _ in range(m)]

    # 초깃값 넣기
    dp[0] = board[0]
    for i in range(m):
        dp[i][0] = board[i][0]

    # dp 실행
    for x in range(1, m):
        for y in range(1, n):
            if board[x][y] == 1 :
                dp[x][y] = min(dp[x - 1][y], dp[x - 1][y - 1], dp[x][y - 1]) + 1

    # max 확인
    mx = 0
    for i in range(m):
        for j in range(n):
            if mx < dp[i][j]:
                mx = dp[i][j]
    return mx * mx

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])

