import math


def check_prime(x):
    # 1,2일때
    if x in (1,0):
        return False
    if x == 2:
        return True

        # 2보다 클때에
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        return True


def to_int(x):
    s = ''.join(x)
    return int(s)


def solution(numbers):
    import itertools
    lst = []

    for i in range(1, len(numbers) + 1):
        temp = list(itertools.permutations(numbers, i))
        temp = list(map(to_int, temp))
        lst.extend(temp)

    lis = list(set(lst))
    return sum(list(map(check_prime,lis)))
