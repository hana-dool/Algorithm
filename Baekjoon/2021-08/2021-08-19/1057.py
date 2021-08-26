import sys
from collections import deque
input = sys.stdin.readline
N ,kim , lim = map(int,input().rstrip().split())
lst = [kim,lim]
lst.sort(reverse= True)

order = list(range(1,N+1))

# 규칙 : N % 2 + N // 2 가 같은것들
cnt = 0
def when_meat(order):
    global cnt
    while len(order) != 1 :
        cnt += 1
        temp = deque([])
        if len(order) % 2 == 1 :
            val = order.pop()
            temp.appendleft(val)
        l = len(order)
        while order :
            end1 = order.pop()
            end2 = order.pop()
            if [end1,end2] == lst :
                return
            elif end1 in lst :
                temp.appendleft(end1)
            elif end2 in lst :
                temp.appendleft(end2)
            else :
                temp.appendleft(end1)
        order = list(temp)
when_meat(order)
if cnt == 0 :
    print(-1)
else :
    print(cnt)


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
#