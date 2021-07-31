from collections import deque


def solution(n, computers):
    ch = [0] * n
    for i in range(n):
        computers[i][i] = 0
    q = deque([])
    q.append(0)
    ch[0] = 1
    while q:
        x = q.popleft()
        for i, v in enumerate(computers[x]):
            if v == 1 and ch[i] == 0:
                q.append(i)
                ch[i] = 1
    return ch


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))