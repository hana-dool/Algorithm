n,k = map(int,input().strip().split())
lst = list(map(int,list(input())))
stk = []
v = k

for i in range(n):
    while v > 0 and stk and stk[-1] < lst[i]:
        stk.pop()
        v -= 1
        print(stk)
    stk.append(lst[i])
print(''.join(map(str,stk[:n-k])))