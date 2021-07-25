def ch(n):
    return n*(n+1) // 2

N = int(input())
x = 1
while True :
    if ch(x) <= N :
        x = x+1
    else : # 처음으로 ch(x) >= N 된 순간 !
        print(x-1)
        break

