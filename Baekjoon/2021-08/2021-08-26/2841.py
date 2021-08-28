import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline
N,P = map(int,input().split())
dic = defaultdict(list)

for _ in range(N) :
    number,pret = map(int,input().split())
    dic[number].append(pret)
dic = dict(dic)
# [8,10,12,10,5]
#
def cnt_move(lst) :
    cnt = 0
    lst = deque(lst)
    stack = []
    while lst :
        val = lst.popleft()
        if not stack : # 스택이 비어있으면
            stack.append(val)
            cnt += 1
        else : # 스택이 차있으면
            if stack[-1] == val : # 마지막과 값이 같으면 그냥 끝~
                continue
            elif stack[-1] > val : # 앗.. 나보다 큰 값이 있네 ?
                while stack : # 스택이 있으면..
                    if stack[-1] > val :
                        stack.pop()
                        cnt += 1
                    elif stack[-1] == val :
                        break
                    elif stack[-1] < val :
                        stack.append(val)
                        cnt += 1
                if not stack :
                    stack.append(val)
                    cnt += 1
            elif stack[-1] < val :
                stack.append(val)
                cnt += 1
    return cnt

cnt = 0
for lst in dic.values() :
    cnt += cnt_move(lst)
print(cnt)