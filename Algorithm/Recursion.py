
def DFS(x):
    if x >= 0 :
        DFS(x-1)
        print(x)
    else :
        return
DFS(5)