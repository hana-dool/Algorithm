import sys
n = int(input())
stack = [0]
ans = []
i = 1
for _ in range(n):
    x = int(input())
    while True :
        if stack[-1] < x :
            if i == n+1:
                print('NO')
                sys.exit(0)
            else :
                stack.append(i)
                ans.append('+')
                i = i+1
        elif stack[-1] == x :
            stack.pop()
            ans.append('-')
            break
        else :
            stack.pop()
for i in ans :
    print(i)