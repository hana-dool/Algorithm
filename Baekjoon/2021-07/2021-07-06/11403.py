def solution(board, moves):
    length = len(board)
    cnt = 0
    stck = []
    for j in moves:
        for i in range(length):
            if board[i][j-1] != 0 : # 하나라도 인형을 만나면
                stck.append(board[i][j-1])
                board[i][j-1] = 0
                if len(stck) >= 2 :
                    if stck[-1] == stck[-2] :
                        stck.pop()
                        stck.pop()
                        cnt += 2
                break
    answer = cnt
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	, [1,5,3,5,1,2,1,4]))





m=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m[0][1]