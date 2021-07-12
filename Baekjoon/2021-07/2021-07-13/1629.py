a,b,c = map(int,input().split())

def power(a,b):
    if b == 1:
        return a
    else :
        val = power(a,b//2)
        if b % 2 == 0 :
            return val * val
        else :
            return val * val * a



power(a,b)