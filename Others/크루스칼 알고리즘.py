# def find_parent(parent,x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을떄까지 재귀적으로 호출된다.
#     if parent[x] != x :
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]
#
# # 두 원소가 속한 집합 합치기
# def union_parent(parent,a,b) :
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a<b :
#         parent[b]=a
#     else :
#         parent[a]=b
#
# # 노드의 개수와 간선(union 연산) 갯수 입력
#
# v,e = map(int,input().split())
# parent = [0] * (v+1)
#
# # 모든 간선을 담을 리스트와 최종 비용 담을 변수
# edges = []
# result = 0
#
# # 부모 테이블 상에서 부모를 자기 자신으로 초기화
# for i in range(1,v+1) :
#     parent[i] = i
#
# # 모든 간선정보 입력받기
# for _ in range(e) :
#     a,b,cost = map(int,input().split())
#     # 비용순으로 정렬하기 위해서 튜플의 첫번쨰 원소를 비용으로 결정
#     edges.append((cost,a,b))
#
# # 간선을 비용순으로 정렬
# edges.sort()
#
# # 간선을 하나씩 확인
# for edge in edges :
#     cost , a, b = edge
#     # 사이클이 발생하지 않는 경우에만 포함
#     if find_parent(parent,a) != find_parent(parent,b) :
#         union_parent(parent,a,b)
#         result += cost
# print(result)


# v,e = map(int,input().split())
#
# edges = []
# for _ in range(e) :
#     start , end , cost = map(int,input().split())
#     edges.append((cost,start,end))
#
# edges.sort()
#
# parent = [0] * (v+1)
# for i in range(1,v+1):
#     parent[i] = i
#
# def find_parent(parent, x) :
#     if parent[x] != x :
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]
#
# def union_parent(parent,a,b) :
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a<b:
#         parent[b] = a
#     else :
#         parent[a] = b
# result = 0
#
# for i in edges :
#     cost ,a,b = i
#     if find_parent(parent,a) != find_parent(parent,b) :
#         union_parent(parent,a,b)
#         result += cost
# print(result)

v,e = map(int,input().split())
