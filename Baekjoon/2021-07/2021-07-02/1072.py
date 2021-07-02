# x : 게임 횟수
# y : 이긴 게임
# z 는 승률 , 소숫점 버림!
import math

x,y = map(int,input().split())
# 이분탐색의 냄새가 솔솔~

def binary(i):
    nx = x + i
    ny = y + i
    val = math.floor(ny*100/nx) - math.floor(y*100/x)
    return(val)



# x / y
# 2x / x+y



i = 0
while True :
    nx = x + i
    ny = y + i
    if math.floor(ny*100/nx) - math.floor(y*100/x) == 1 :
        print(i)
        break
    i += 1
