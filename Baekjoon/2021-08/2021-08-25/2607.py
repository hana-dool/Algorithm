import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
lst = []
init_strng = input()
cnt = 0
for _ in range(N-1) :
    strng = input()
    dic = defaultdict(int)
    for i in strng :
        dic[i] += 1
    for s in init_strng :
        dic[s] -= 1
    dic = dict(dic)
    # 더하거나
    # 빼거나
    # 하나를 다른 문자로 바꾸거나
    lst = [0,0]
    k = 0
    for i in dic.values() :
        if i == 0 :
            pass
        elif i == 1 :
            lst[0] += 1
        elif i == -1 :
            lst[1] += 1
        else :
            k = 1
            break
    if lst in ([1,1],[1,0],[0,1],[0,0]) :
        gg = 1
    else :
        gg = 0
    if k == 1 :
        continue
    else :
        cnt += gg
print(cnt)


