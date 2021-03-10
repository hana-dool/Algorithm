# https://www.acmicpc.net/problem/1978
import sys
read = sys.stdin.readline

N = int(read())
lis = map(int,read().split())
cnt = 0

def Prime(x):
    check = 0
    if x == 1 :
        return(-1)
    for divisor in range(2,int(x**(0.5))+1) :
        if x % divisor == 0 :
            check = 1 # 한번이라도 나누어 떨어지면 1 으로 바뀌고
            break # break 가 걸린다.
    if check == 0:
        return(1) # check 가 0 이라는것은 나누어떨어짐이 없엇음. 즉 소수
    else :
        return(-1)

cnt = 0
for val in lis :
    if Prime(val) == 1 :
        cnt += 1
print(cnt)
