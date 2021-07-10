#
# 1 2 0


# 2 3 1 그냥 각각에 대해서, 순위를 매겨주면 됨~
N = int(input())
lst = list(map(int,input().split()))
ans = [0] * N
i = 0
while True :
    if min(lst) == 10**9:
        break
    idx = lst.index(min(lst))
    lst[idx] = 10**9
    ans[idx] = i
    i += 1
for i in ans:
    print(i, end = ' ')
# B[1] = 2
# B[2] = 3
# B[0] = 1


# 음....
# 1 2 3