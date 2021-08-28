import sys
input = sys.stdin.readline
M = int(input())
S = set()
def add(x) :
    S.add(x)

def Remove(x):
    if x in S :
        S.remove(x)

def check(x) :
    if x in S :
        return 1
    else :
        return 0

def toggle(x) :
    if x in S :
        S.remove(x)
    else :
        S.add(x)

def All() :
    return set(range(1,21))

def empty() :
    return set()

for _ in range(M) :
    strng = input().strip()
    if ' ' in strng :
        a,b = strng.split()
        b = int(b)
    else :
        a = strng
    if a == 'add' :
        add(b)
    elif a == 'check' :
        print(check(b))
    elif a == 'remove' :
        Remove(b)
    elif a == 'toggle' :
        toggle(b)
    elif a == 'all' :
        S = All()
    elif a == 'empty' :
        S = empty()
