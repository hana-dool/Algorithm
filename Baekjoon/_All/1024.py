# N , L 이 주어질 떄 합이N 이면서 길이가 적어도 L인
# 가장 짧은 연속된 음이 아닌 정수 리스트를 수하는 프로그램 구하라

import sys
read = sys.stdin.readline
N,L = map(int,read().split())
# 길이가 적어도 L 인 연속된 음이 아닌 정수 리스트를 출력해야 한다.

#  #  m m+1 ... m+k 에 대해서
# m(k+1)+k(k+1)/2 -> [m + k/2](k+1) = N ;  k >= L-1
# 즉 위 수식을 만족하는 m,k 쌍을 찾는것이 목적
# N 에 관한 식이기 때문에 k 를 고정한다고 하였을 떄에 N 에 관한 1차식이 나옴
# [N - k(k+1)/2]/(k+1) 이 int 라면 good
# k 는 최대 L 까지 가능

k = L - 1 # k 는 계~속 커짐.
while True :
    m = (N - k*(k+1)/2)/(k+1) # 이 값은 m 이 나온다.
    if k > 99 :
        print(-1)
        break
    if m < 0 :
        k += 1
    else :
        if m == int(m):
            for i in range(k+1):
                print(int(m)+i,end = ' ')
            break
        else :
            k += 1