M = int(input())
m = 1000 - M
lis = [500,100,50,10,5,1]
cnt = 0
for i in lis:
    if int(m) != 0 :
        cnt += m // i
        m = m % i
print(cnt)