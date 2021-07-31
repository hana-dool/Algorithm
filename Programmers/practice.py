def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을떄까지 재귀적으로 호출된다.
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

find_parent([0,0,0,2,3],3)