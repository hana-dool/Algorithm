def gcd(x,y):
    while x%y != 0 :
        x,y = y,x%y
    return y

v = sorted('13253')
print(v)


lst = [1,2,3,4,5,6,7,8,9]
lst[20:34]

tuple([lst[3]]+lst[:3]+lst[4:])
s = "ZbBcdDefg"
sorted(s)



def convert(n, base):
    T = "0123456789ABCDEF"
    q = n // base
    r = n % base
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

convert(35,2)