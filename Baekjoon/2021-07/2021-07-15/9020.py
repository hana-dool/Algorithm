# 우선 소수를 찾아야 한다.

import sys
input = sys.stdin.readline

n = int(input())
import math
prime = [0]*10001
for i in range(2,101):
    for j in range(i*2,10001,i):
        prime[j] = 1
st = set()
for i in range(2,10001) :
    if prime[i] == 0 :
        st.add(i)

for _ in range(n):
    k = int(input())
    ans = []
    for i in st :
        if k-i in st :
            ans.append((i,k-i))
    mn = 99999
    rst = (0,0)
    for i in ans :
        if abs(i[1] - i[0]) < mn :
            mn = abs(i[1] - i[0])
            rst = i
    print(rst[0],end=' ')
    print(rst[1])

