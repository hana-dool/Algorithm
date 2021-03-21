


import sys
read = sys.stdin.readline

# 유클리드 호제법을 통해 gcd 를 구함
# a a*1 .... a*b , b*1 ... b*a 까지 다 구한다음에, 일치하는거 구하는형식으로 하면 시간초과
def gcd(x,y): # 앞의 값이 나눠지는값
    if x % y == 0 :
        return(y)
    else :
        return gcd(y , x%y)

def lcm(x,y): # x,y 의 lcm 을 구한다.
    ans = x*y//gcd(x,y)
    return(ans)

T = int(read())
for _ in range(T):
    A,B = map(int,read().split())
    print(lcm(A,B))
