import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline



n,m = map(int,input().split())
parent = list(range(n+1))

def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    if find_parent(parent,a) != find_parent(parent,b) :
        a_p = find_parent(parent,a)
        b_p = find_parent(parent,b)
        if a_p < b_p :
            parent[b_p] = a_p
        else :
            parent[a_p] = b_p

for _ in range(m):
    oper,a,b = map(int,input().split())
    if oper == 0 :
        union_parent(parent,a,b)
    elif oper == 1 :
        if find_parent(parent,a) == find_parent(parent,b) :
            print('YES')
        else :
            print('NO')