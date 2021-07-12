n = int(input())
cnt = 0
def dfs(lst):
    global cnt
    if len(lst) == n :
        cnt += 1
        return
    candidate = list(range(n))
    for i in range(len(lst)):
        if lst[i] in candidate :
            candidate.remove(lst[i])
        if lst[i] + len(lst) - i  in candidate :
            candidate.remove(lst[i] + len(lst) - i)
        if lst[i] - len(lst) + i in candidate :
            candidate.remove(lst[i] - len(lst) + i)
    if candidate:
        for x in candidate :
            lst.append(x)
            dfs(lst)
            lst.pop()

for i in range(n):
    dfs([i])
print(cnt)
