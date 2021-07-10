T = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    distance = y - x
    i = 0
    while True :
        i += 1
        val = i * (i + 1) + (i+1) # 1 2 .... i i+1 i .....
        if distance < val :
            break
     # 1 2 ....i-1 i i-1
    if distance - (i-1) *(i) - i == 0 :
        print(2*(i-1)+1)
    elif distance - (i-1) *(i) - i  > i :
        print(2*(i-1)+1+2)
    else :
        print(2*(i-1)+1+1)
