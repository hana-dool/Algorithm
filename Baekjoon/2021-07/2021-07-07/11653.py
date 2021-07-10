n = int(input())
k = n
divisor = 2
while True :
    if divisor > k :
        break
    if n % divisor == 0 :
        print(divisor)
        n = n // divisor
    else :
        divisor += 1