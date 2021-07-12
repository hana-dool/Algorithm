n = int(input())
# 버리고, 위에있는 카드를 젤 아래로 옮기기

from collections import deque
lst = deque(list(range(1,n+1)))
while lst :
    val1 = lst.popleft()
    if lst :
        val2 = lst.popleft()
        lst.append(val2)
    else :
        break
print(val1)