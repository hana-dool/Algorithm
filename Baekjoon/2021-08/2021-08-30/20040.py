import sys
input = sys.stdin.readline
N , M = map(int,input().split())
parent = list(range(N))

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
        return False
    else :
        return True
cnt = 0
for _ in range(M) :
    start, end = map(int,input().split())
    cnt += 1
    if union_parent(parent,start,end) :
        print(cnt)
        sys.exit(0)
print(0)

