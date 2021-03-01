import sys
read = sys.stdin.readline

N,M,V = map(int,read().split())
# N : 정점의 갯수
# M : 간선의 갯수
# V : 탐색을 시작할 정점의 번호 V

# DFS 와 BFS 로 탐색한 결과를 출력하는 프로그램을 작성하라.
# 1. 그래프 문제이므로, matrix 부터 시작한다.

# M+1 인 이유는 인덱싱의 편리성 때문이다.
mat = [[0]*(M+1) for _ in range(M+1)]

for _ in range(M) :
    a,b = map(int,read().split())
    mat[a][b] = mat[b][a] = 1

ch = [0]*(N+1) # 정점의 갯수 list

def DFS(x,path):
    ch[x] = 1 # 점유상태를 먼저 표현한다.
    print(path[-1], end = ' ') # print 만 한다.
    for i in range(1,N+1) : # 1~N 개의 가능성에 대해서 (1~N 이기 떄문에 빠른 IDX 부터 search 하는것과 같음)
        if mat[x][i] == 1 and ch[i]==0 : # 경로가 있고, 지나온곳이 아니라면
            ch[i] = 1
            DFS(i,path+[i]) # 그곳으로 이동한다.


# BFS 는 기본적으로 queue 구조를 답습한다.
def BFS(V):
    ch = [0] * (N + 1)  # 정점의 갯수 list
    ans = []
    ch[V] = 1
    que = [V]
    while que:
        t = que.pop(0)
        print(t,end = ' ')
        for i in range(1,N+1):
            if mat[t][i] == 1 and ch[i] == 0:
                que.append(i)
                ch[i] = 1

DFS(V,[V])
print()
BFS(V)