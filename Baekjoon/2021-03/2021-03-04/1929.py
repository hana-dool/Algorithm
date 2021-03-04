# https://www.acmicpc.net/problem/1929
import sys
read = sys.stdin.readline

N, M = map(int,read().split())
if N == 1 :
    N += 1

import math


def Prime(start,end) : # start ~ end 까지 소수들을 조사
    val = 0
    pr = -1
    for i in range(start,end+1):
        pr = 0 # prime 을 발견하면 0 그대로일것
        for divisor in range(2,int(math.sqrt(i))+1):
            if i % divisor == 0:
                pr = 1 # 소수가 아님
                break # 응 이제 볼 필요 없어~
        if pr == 0 : # 아
            val = i # break 안만나고 잘 내려오면!
            break
    if pr == 0 :
        return(val)
    else :
        return(-1)

# Prime 함수는 start ~ end 까지의 값 중 가장 가까운 소수를 뽑아낸다.
# 아 1은 소수가 아니구나!

while True :
    t = Prime(N, M)
    N = t + 1
    if t == -1 :
        break
    else :
        print(t)
