# 1초 (1000번)
# 10000
m = int(input())
n = int(input())
import math
def find(x):
    if x == 1 :
        return
    else :
        for i in range(2,round(math.sqrt(x))+1):
            if x % i == 0 :
                return
        else :
            return x
ans = []
for i in range(m,n+1):
    if find(i):
        ans.append(find(i))
if len(ans) == 0 :
    print(-1)
else :
    print(sum(ans))
    print(ans[0])