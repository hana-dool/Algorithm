N = int(input())
cnt = 0
k = 1
while True :
    if N // 5**k == 0 :
        break
    else :
        k += 1

for i in range(1,k+1) :
    cnt += N // 5**i

print(cnt)

