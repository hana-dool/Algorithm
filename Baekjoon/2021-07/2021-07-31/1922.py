import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

# 크루스칼 알고리즘
edge = []
for _ in range(M) :
    start,end,cost = map(int,input().split())
    edge.append((cost,start,end))

# 서로소 알고리즘
# 현재 부모는 늘 자식보다 작은 값을 가집니다.
def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x]) # parent[x] 에 기어이, 부모 노드를 넣음
    return parent[x]

def union_parent(parent,a,b) : # a와 b 를 합치는 연산
    a_p = find_parent(parent,a)
    b_p = find_parent(parent,b)
    if a_p > b_p :
        parent[a_p] = b_p
    else :
        parent[b_p] = a_p  # 다른 경우에는, b_p 의 부모는 a_p 가 됩니다.
parent = list(range(0,N+1))
# 각각의 노드는 , 자기 자신을 우선 부모로 가짐
# 첫번쨰 값인 0 은 사실 , 0임...
rst = 0
# 크루스칼 알고리즘 시작
edge.sort()
for e in edge :
    cost,start, end = e
    if find_parent(parent, start) != find_parent(parent, end) :
        union_parent(parent,start,end)
        rst += cost
print(rst)