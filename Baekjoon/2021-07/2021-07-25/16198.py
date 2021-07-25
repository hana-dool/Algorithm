# dfs 입니다.
# bfs 인가.. ?
# 뭐 어쩃든

N = int(input())
lst = list(map(int,input().split()))
ans = []
def dfs(l,val,lst) :
    if l == 2 :
        ans.append(val)
        return
    else :
        for i in range(1,l-1) :
            dfs(l-1,val + lst[i-1]*lst[i+1],lst[:i]+lst[i+1:])
dfs(len(lst),0,lst)
print(max(ans))



