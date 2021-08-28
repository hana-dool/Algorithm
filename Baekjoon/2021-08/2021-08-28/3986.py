import sys
input = sys.stdin.readline
N = int(input())
# ABBBAB

def check_good(strng) :
    if len(strng) % 2 == 1 :
        return False
    elif strng.count("A") % 2 == 1 or strng.count("B") % 2 == 1 :
        return False
    else :
        if 'ABAB' in strng :
            return False
        elif 'BABA' in strng :
            return False
    return True

cnt = 0
for _ in range(N) :
    temp = input().strip()
    new = []
    for i in temp :
        if not new :
            new.append(i)
        else :
            if new[-1] == i :
                new.pop()
            else :
                new.append(i)
    new_strng = ''.join(new)
    if check_good(new_strng) :
        cnt += 1
print(cnt)

# AABBAB