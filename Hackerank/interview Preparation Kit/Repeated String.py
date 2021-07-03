def repeatedString(s,n):
    l = len(s)
    c = s.count('a')
    rp = n // l
    resid = n % l
    ans = c * rp + s[:resid].count('a')
    return(ans)

repeatedString('a',1000)

x = 3
lst = [3,2]
d = 3 + 3