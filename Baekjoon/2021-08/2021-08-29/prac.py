from collections import defaultdict


N = 7
edges = [(1,2),(1,5),(2,3),(2,6),(3,4),(6,4),(4,7),(7,6)]
graph = defaultdict(list)
# 그래프 만들기
for edge in edges :
    v,w = edge
    graph[v].append(w)

# visited 만들기
visited = [0]*(N+1)

# 중요!
def dfs(start, here):
    if visited[here]:
        if start == here:
            return True # 사이클이 맞다!
        return False # 같지 않으면 다른 노드에서 온것.
    visited[here] = True # 방문처리
    for node in graph[here]:
        if dfs(start, node):
            return True
    return False

for i in range(1,N+1) :
    if dfs(i,i) :
        print(True)
        break
else :
    print(False)