m,n = map(int,input().split())
import math
gcd = 1
for i in range(1,max(m,n)+1):
    if m % i == 0 and n % i ==0 :
        if gcd < i :
            gcd = i
print(gcd)
print(m*n//gcd)

