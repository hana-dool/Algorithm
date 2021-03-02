def push(main,x):
    main.append(x)

def pop(main):
    if len(main) < 1 :
        print(-1)
    else :
        v = main.pop(0)
        print(v)

def size(main):
    print(len(main))

def empty(main):
    if len(main) >= 1 :
        print(0)
    else :
        print(1)

def front(main):
    if len(main) >= 1 :
        print(main[0])
    else :
        print(-1)

def back(main):
    if len(main) >= 1 :
        print(main[-1])
    else :
        print(-1)

import sys
read = sys.stdin.readline
N = int(read())

lis = []
for _ in range(N) :
    a = list(read().split())
    if len(a) >= 2 :
        all,num = a
        num = int(num)
        push(lis,num)
    else :
        if a[0] == 'pop':
            pop(lis)
        elif a[0] == 'size':
            size(lis)
        elif a[0] == 'empty':
            empty(lis)
        elif a[0] == 'front' :
            front(lis)
        elif a[0] == 'back' :
            back(lis)