# import sys
# input = sys.stdin.readline
#
# inf = 10**9
# n = int(input())
# m = int(input())
#
# graph = [[inf]*(n+1) for _ in range(n+1)]
#
# for i in range(n+1):
#     for j in range(n+1):
#         if i == j :
#             graph[i][j] = 0
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     if graph[a][b] > c:
#         graph[a][b] =  c
#
# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if graph[i][j] == inf :
#             print('0',end = ' ')
#         else :
#             print(graph[i][j], end = ' ')
#     print()








#
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = 10**9
graph = [[inf] * (n+1) for _ in range(n+1)]
for i in range(n+1) :
    graph[i][i] = 0
for _ in range(m):
    start,end,cost = map(int,input().split())
    if graph[start][end] > cost :
        graph[start][end] = cost

for k in range(1,n+1) :
    for i in range(1,n+1):
        for j in range(1,n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1) :
    for j in graph[i][1:] :
        if j == inf :
            print(0, end = ' ')
        else :
            print(j, end = ' ')
    print()