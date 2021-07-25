def gcd(x,y):
    while x % y != 0 :
        x,y = y , x % y
    return y
import itertools

T = int(input())
for _ in range(T):
    ans = 0
    lst = list(map(int,input().split()))
    lst = lst[1:]
    for i in list(itertools.combinations(lst,2)) :
        ans +=  gcd(int(i[0]),int(i[1]))
    print(ans)

