def fact(x):
    if x == 0:
        return 1
    val = 1
    while x > 0 :
        val = x * val
        x = x-1
    return(val)

n,k = map(int,input().split())

ans = fact(n) // (fact(n-k) * fact(k))

print(int(ans) % 10007)