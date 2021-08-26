
lst = []
for _ in range(9) :
    lst.append(int(input()))

from itertools import combinations

comb = list(combinations(lst,7))
for i in comb :
    if sum(i) == 100 :
        ans = i
rst = list(ans)
rst.sort()
for i in rst :
    print(i)