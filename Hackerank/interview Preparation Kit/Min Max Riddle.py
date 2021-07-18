def riddle(arr): # brtue Force...
    l = len(arr)
    rst = []
    for i in range(l): # 길이
        lst = []
        for j in range(l-i+1): # 시작지점
            lst.append(min(arr[j:j+i]))
        rst.append(max(lst))
    print(*rst)

from collections import deque
q=deque([(0,0)])
q.popleft()




for x in range(0):
    print(x)