E,S,M = map(int,input().split())
e = E % 15
s = S % 28
m = M % 19
i = 1
while True :
    i_e = i % 15
    i_s = i % 28
    i_m = i % 19
    if i_e == e and i_s == s and i_m == m :
        print(i)
        break
    else :
        i += 1
