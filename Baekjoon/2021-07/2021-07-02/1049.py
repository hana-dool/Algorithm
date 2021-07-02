# n : 끊어진 기타줄의 갯수
# m : 기타 줄 상품 m 개
# a,b : 기타죽 6개 가격 / 1개살때 가격
n,m = map(int,input().strip().split())
p_6 = []
p_1 = []
for _ in range(m):
    a,b = map(int,input().strip().split())
    p_6.append(a)
    p_1.append(b)
m6 = min(p_6)
m1 = min(p_1)


if m1*6 < m6 :
    print(m1*n)
else :
    n6 = n // 6
    n1 = n % 6
    if m6 < n1*m1:
        print(n6 * m6 + m6)
    else :
        print(n6 * m6 + n1 * m1)
