from collections import defaultdict
N = 7
edges = [(1, 2), (2, 3), (3, 4), (4, 2), (5, 6), (6, 7)]
graph = defaultdict(list)
for edge in edges:
    v, w = edge
    graph[v].append(w)
visited = [0] * (N + 1)

def dfs(here) :
    if visited[here] == -1 : # 어 이미 방문했어?
        return True
    if visited[here] == 1 :
        return False
    visited[here] = -1
    for node in graph[here] :
        if dfs(node) :
            return True
    visited[here] = 1
    return False
dfs(6)
