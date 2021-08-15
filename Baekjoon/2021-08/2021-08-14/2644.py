import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a,b = map(int,input().split())
m = int(input())

graph = [[] for _ in range(N+1)]
ch = [0] * (N+1)

for _ in range(m) :
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque([(a,0)])
ch[a] = 1
def bfs() :
    while q  :
        x,cnt = q.popleft()
        if x == b :
            print(cnt)
            return
        for i in graph[x] :
            if ch[i] == 0 :
                ch[i] = 1
                q.append((i,cnt+1))
    print(-1)
bfs()

