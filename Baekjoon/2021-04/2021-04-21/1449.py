# https://www.acmicpc.net/problem/1449

# 4 4
# 1 2 3 4
# 무조건 0.5 간격으로 붙이는게 유리함



import sys
read = sys.stdin.readline
N, L = map(int,read().split())
lst = list(map(int,read().split()))
lst.sort()
cnt = 1
f = lst.pop(0)
while lst :
    if lst[0] >= f + L :
        cnt += 1
        f = lst.pop(0)
    else :
        lst.pop(0)
print(cnt)

