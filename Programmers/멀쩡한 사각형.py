def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y


def solution(w, h):
    resid = w + h - 1 - (gcd(w, h) - 1)
    answer = w * h - resid
    return answer

