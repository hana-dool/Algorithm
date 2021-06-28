# import sys
# read = sys.stdin.readline
# from collections import deque
#
# def bfs(v, target):
#     count = 0
#     q = deque([[v, count]])
#     while q:
#         value = q.popleft()
#         v = value[0]
#         count = value[1]
#         if v == target:
#             return count
#
#         if not visited[v]:
#             count += 1
#             visited[v] = True
#             for e in adj[v]:
#                 if not visited[e]:
#                     q.append([e, count])
#     return -1
#
#
# n = int(input())
# q1, q2 = map(int, input().split())
# m = int(input())
# adj = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     adj[x].append(y)
#     adj[y].append(x)
# print(bfs(q1, q2))


def bfs(graph, start_node):
    visit = list()
    queue = list()
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))

