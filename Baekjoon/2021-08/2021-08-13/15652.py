N , M = map(int,input().split())
mapping = range(1,N+1)
def dfs(lst) :
    if len(lst) == M :
        print(*lst)
        return
    else :
        for val in mapping :
            if not lst :
                dfs(lst+[val])
            elif lst[-1] <= val :
                dfs(lst+[val])


dfs([])
