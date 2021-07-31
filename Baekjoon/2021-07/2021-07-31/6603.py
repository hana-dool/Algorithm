import sys
input = sys.stdin.readline
lst = [1]
from itertools import combinations

while True :
    lst = list(map(int,input().split()))
    if lst == [0] :
        break
    else :
        lst.pop(0)
        select = list(combinations(lst,6))
        select.sort()
        for i in select :
            ans = list(map(int,i))
            print(*ans)
        print()


