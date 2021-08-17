import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = list(range(N+1))

mat = [list(map(int,input().split())) for _ in range(N)]

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    if find_parent(parent,a) != find_parent(parent,b) :
        a_p = find_parent(parent,a)
        b_p = find_parent(parent,b)
        if a_p < b_p :
            parent[b_p] = a_p
        elif b_p < a_p :
            parent[a_p] = b_p

for x in range(N) :
    for y in range(N) :
        if mat[x][y] == 1 :
            union_parent(parent,x+1,y+1)

wt_visit = list(map(int,input().split()))

v = find_parent(parent,wt_visit[0])
for city in wt_visit :
    if v != find_parent(parent,city) :
        print('NO')
        break
else :
    print('YES')

