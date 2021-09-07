import sys
input = sys.stdin.readline
V , E = map(int,input().split())
parent = list(range(V+1))

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a_p = find_parent(parent,a)
    b_p = find_parent(parent,b)
    if a_p != b_p :
        if a_p < b_p :
            parent[b_p] = a_p
        else :
            parent[a_p] = b_p

lst = []
for _ in range(E) :
    a,b,cost = map(int,input().split())
    lst.append((cost,a,b))
lst.sort()

cnt = 0
for edge in lst :
    cost , a, b = edge
    if find_parent(parent,a) == find_parent(parent,b) :
        continue
    else :
        union_parent(parent,a,b)
        cnt += cost
print(cnt)
