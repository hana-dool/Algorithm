
# 내 제출, 1초제한 / 80ms
# 이 경우 중요한점은 '단위가 커질수록 그 이전값의 배수만큼 커진다.' 라는것이다.
# 이 점에서 착안하면, 제일 큰 값부터 최대한 Greedy 하게 채워넣어도 제익 적은 수가 된다.
import sys
read = sys.stdin.readline
N,K = map(int,read().split())

price = []
for _ in range(N):
    price.append(int(read()))
price = price[::-1]

cnt = 0

for val in price :
    if K == 0 :
        break
    cnt += K // val
    K = K % val

print(cnt)


# 다른사람 풀이
N, K = map(int, input().split())
l = [int(input()) for _ in range(N)]
# list comprehension! 훨씬 쉽고 보기좋음
# append 보다 성능이 좋은듯?

l.reverse()
cnt = 0

for i in l:
    cnt += K//i
    K %= i

print(cnt)

