from collections import deque
N,K = map(int,input().split())

q = deque([(N,0)]) # 현재 위치 + 초
ch = [0]*250000

while q :
    now = q.popleft()
    if now[0] == K :
        break
    else :
        for i in [now[0]-1,now[0]+1,now[0]*2] :
            if 0 <= i < 250000 :
                if ch[i] == 0:
                    ch[i] = 1
                    q.append((i,now[1]+1))
print(now[1])