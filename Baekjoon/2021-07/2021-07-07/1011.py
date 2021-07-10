# 처음은 1
# k 이동 후에는 k-1 k k+1
# 2초
# 1억


# dp ?
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    distance = y-x
    step = 1
    half = distance // 2
    while True :
        if distance - step < half :
            distance = distance - step
        step += 1


# 1 2 3 2 1
# 보니까.... 어짜피 half 까지는 가고..
# 123 을 이용하여 n 을 만드는 가짓수를 출력해라.. 이건데?
# dp

# 반까지는 1 + 2 ... 로 가다가
# 그 다음에는 급속도로 빡! 줄여나가야하는것.. GREEDY~!
# [0 1 2 2 3 3 3 4 4 4 4 5 5 5 ]