import sys
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

from collections import deque
visit = [0] * (N+1)

q = deque([1])
visit[1] = 1

ans = [0]* (N+1)

while q :
    x = q.popleft()
    for i in tree[x]:
        if visit[i] == 0 :
            ans[i] = x
            visit[i] =1
            q.append(i)

for i in ans[2:]:
    print(i)