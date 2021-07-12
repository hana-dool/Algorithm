def solution(m, n, board):
    mat = []
    for i in board :
        mat.append(list(i))
    mat2 = []
    for i in range(n) :
        stck = []
        for j in range(m):
            stck.append(mat[j][i]) # 위에꺼부터 들어오는 스택
        stck.reverse()
        mat2.append(stck) # 스택의 append
    ch = [[0]*m for _ in range(n)]
    while True :
        print(mat2)
        for i in range(n-1): # len(mat[i])-1
            for j in range(min(len(mat2[i])-1,len(mat2[i+1])-1)):
                if mat2[i][j] == mat2[i+1][j] == mat2[i][j+1] == mat2[i+1][j+1]:
                    ch[i][j] = ch[i+1][j] = ch[i][j+1] = ch[i+1][j+1] = 1
        val = 0
        for i in range(n):
            for j in range(len(mat2[i])-1):
                val += ch[i][j]
        if val == 0 :
            break
        for i in range(n):
            # 열끼리 본다.
            for j in range(len(mat2[i])-1):
                if ch[i][j] == 1 :
                    mat2[i][j]  = 0# 싸악 삭제
        for i in range(n):
            stck = []
            for j in range(len(mat2[i])-1):
                if mat2[i][j] != 0 :
                    stck.append(mat2[i][j])
            mat2[i] = stck
        # ch 초기화
        for i in range(n):
            for j in range(m):
                ch[i][j] = 0
    print(mat2)
    answer = 0
    return answer

solution(6,6,["TTTANT",
              "RRFACC",
              "RRRFCC",
              "TRRRAA",
              "TTMMMF",
              "TMMTTJ"])