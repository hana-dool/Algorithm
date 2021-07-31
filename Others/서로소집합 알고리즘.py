from collections import deque
# 노드의 갯수와 간선 갯수 입력
v,e = map(int,input().split())

# 모든 노드에 대해 진입 차수는 0으로 초기화하기
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e) :
    a,b = map(int,input().split())
    graph[a].append(b) # A  에서 B 로 이동 가능함을 나타냄
    indegree[b] += 1 # 진입차수 1 증가


# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    # 처음 시작할떄에는 진입 차수가 0인 노드를 큐에 삽입해야한다.
    for i in range(1,v+1):
        if indegree[i] == 0 :
            q.append(i)

    # 큐가 빌떄까지 반복
    while q :
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 뺴기기
        for i in graph[now] :
            indegree[i] -= 1
            # 새롭게 진입 차수가 0 이 되는 노드를 큐에 삽입
            if indegree[i] == 0 :
                q.append(i)
    # 결과 출력
    for i in result :
        print(i, end = ' ')

topology_sort()