y,x= map(int,input().split())
import sys
cur = x*100/y
if cur >= 99 :
    print(-1)
    sys.exit(0)

import math

def ch(i):
    if  math.floor((x+i)*100 /(y+i)) - math.floor(cur) >= 1 :
        return(1)
    else :
        return(-1)

start = 0
end = 1000000000

while start <= end :
    mid = (start + end) //2
    if ch(mid) == 1 :
        end = mid - 1
    elif ch(mid) > 1 :
        end = mid - 1
    else :
        start = mid + 1
print(start)
