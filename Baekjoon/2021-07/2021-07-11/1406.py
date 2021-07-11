import sys
input = sys.stdin.readline

ans = list(input().strip())
M = int(input())
cursor = len(ans)
stck = []

for _ in range(M) :
    lst = list(input().strip().split())
    if lst[0] == 'L' :
        if ans :
            stck.append(ans.pop())
    elif lst[0] == 'D' :
        if stck :
            ans.append(stck.pop())
    elif lst[0] == 'B' :
        if ans :
            ans.pop()
    elif lst[0] == 'P' :
        ans.append(lst[1])
rst = ans + stck[::-1]
for i in rst :
    print(i,end='')