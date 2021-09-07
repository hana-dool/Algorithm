import sys
input = sys.stdin.readline
N, M = map(int,input().split())
choice = list(range(1,N+1))

def dfs(lst,visit) :
    if len(lst) == M :
        print(*lst)
        return
    else :
        for i in choice :
            if visit[i] == 0:
                dfs(lst+[i],visit[:i]+[1]+visit[i+1:])
dfs([],[0]*(N+1))
