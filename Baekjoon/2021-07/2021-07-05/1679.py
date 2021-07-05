n,k = map(int,input().split())
import sys
from collections import deque

dic = {n:1}
stck = deque([n])
if n == k :
    print(0)
    sys.exit(0)
while stck :
    x = stck.popleft()
    if x == k:
        print(dic[x]-1)
    if 80001 > x :
        p1 = x * 2
        if not dic.get(p1,0) :
            dic[p1] = dic[x] + 1
            stck.append(p1)
    if 150001 > x > 0 :
        p2 = x-1
        if not dic.get(p2,0) :
            dic[p2] = dic[x] + 1
            stck.append(p2)
    if 150001 > x :
        p3 = x + 1
        if not dic.get(p3,0) :
            dic[p3] = dic[x] + 1
            stck.append(p3)

