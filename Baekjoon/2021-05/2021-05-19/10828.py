import sys
read = sys.stdin.readline

N = int(read())
stk = []
for _ in range(N):
    x = read().strip()
    if x[0:4] == 'push':
        k, val = x.split()
        stk.append(int(val))
    elif x == 'pop':
        if stk :
            s = stk.pop()
            print(s)
        else :
            print(-1)
    elif x == 'top':
        if stk :
            print(stk[-1])
        else :
            print(-1)
    elif x == 'empty':
        if stk :
            print(0)
        else :
            print(1)
    elif x == 'size':
        print(len(stk))
