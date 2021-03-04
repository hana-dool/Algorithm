import sys
read = sys.stdin.readline

N = int(read())
for _ in range(N):
    line = read()
    cond = 0
    check = 0
    for i in line :
        if i == '(':
            cond += 1
        elif i == ')' :
            cond -= 1
        if cond < 0 :  # 중간에 ( 보다 ) 가 많으면 안됨
            check = 1
    if check == 1 :
        print('NO')
    else :
        if cond == 0 : # ( 의 수가 계속 많았고, 나중에는 일치
            print('YES')
        else :
            print('NO') # 수가 맞지 않았음.. ㅜㅜ