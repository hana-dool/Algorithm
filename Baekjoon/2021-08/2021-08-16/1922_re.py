import sys
input  = sys.stdin.readline

N = int(input())
M = int(input())

edges = []

for _ in range(M) :
    start , end , price = map(int,input().split())
    edges.append((price,start,end))

parent = list(range(N+1))
def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a_p = find_parent(parent,a)
    b_p = find_parent(parent,b)
    if a_p != b_p :
        if a_p < b_p :
            parent[b_p] = a_p
        else :
            parent[a_p] = b_p

edges.sort()
cost = 0
for edge in edges :
    if find_parent(parent, edge[1])  != find_parent(parent,edge[2]) :
        union_parent(parent,edge[1],edge[2])
        cost += edge[0]
print(cost)