# https://www.acmicpc.net/problem/1292

import sys
read = sys.stdin.readline
A,B = map(int,read().split())

# B 가 1000까지 이므로.. 우선 n*n+1/2 값의 list 를 구성
lis = [0]
for i in range(1,50):
    lis.append((i * i+1)//2)
# [0,1,2,3,4]
# [0,1,3,6,10] = lis

l = []
for i in range(0,49):
    if lis[i] < B and B <= lis[i+1] : # A 의 값은 i+1
        for _ in range(1,i+2):
            l.extend([_]*_)

print(sum(l[A-1:B]))
