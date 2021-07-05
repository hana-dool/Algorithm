ch = [0]*10000
def d(n):
    while True :
        if n >= 10000:
            break
        else :
            ch[n] = 1
            n = n + sum(list(map(int,list(str(n)))))

for i in range(1,10000):
    if ch[i] == 0 :
        d(i)
        print(i)