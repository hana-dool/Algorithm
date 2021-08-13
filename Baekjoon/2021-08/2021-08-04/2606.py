from collections import defaultdict
from collections import deque
N = int(input())
M = int(input())
dic = defaultdict(list)
for _ in range(M):
    start, end = map(int,input().split())
    dic[start].append(end)
    dic[end].append(start)
graph = dict(dic)
ch = [0] * (N+1)

q = deque([1])
ch[1] = 1
cnt = 0
while q :
    now = q.popleft()
    for i in graph[now] :
        if ch[i] == 0 :
            ch[i] = 1
            cnt += 1
            q.append(i)
print(cnt)
