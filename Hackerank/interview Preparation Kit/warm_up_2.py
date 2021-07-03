from collections import deque
n = 7
gg = 1
def bfs(c):
    global gg
    queue = deque()
    queue.append(0)
    while queue :
        if gg == 0 :
            break
        x = queue.popleft()
        for i in [1,2]:
            nx = x + i
            if nx == n-1 :
                c[nx] = c[x] + 1
                gg = 0
                break
            if nx < n and c[nx] ==0 :
                queue.append(nx)
                c[nx] = c[x] + 1
    print(c[-1])





