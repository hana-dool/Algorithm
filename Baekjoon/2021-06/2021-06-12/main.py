N  = int(input())
ch = [0] * N

def DFS(x):
    if x >= N :
        for i in range(N):
            if ch[i] ==1 :
                print(i+1, end=' ')
        print()
    else :
        ch[x] = 1
        DFS(x+1)
        ch[x] = 0
        DFS(x+1)
DFS(0)