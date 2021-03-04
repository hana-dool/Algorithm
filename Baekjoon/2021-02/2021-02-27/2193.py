import sys
read = sys.stdin.readline

N = int(read())
# 1000
# 1001
# 1010
# recursive 하게 구할 수 있다.
# F(N) 을 주어진 조건에 맞는 이친수라고 하자.
# F(N) = F(N-2)+F(N-3) ....... 이다.
# 첫 자리수는 무조건 1이여야하므로 10 이 고정된다.
# 10 F(N-2) (첫 자리수가 1) + 100F(N-3) + .......
# 0  1  2  3  4  5  6  7
# 1  1  1  2  3  5  8  13 ......
# N = 3이면,
lis = [0,1]
for _ in range(N-1): # N-1번
    val = lis[-1]+lis[-2]
    lis.append(val)

print(lis[-1])