import heapq


def solution(N, road, K):
    inf = 10 ** 9
    distance = [inf] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    # 그래프 생성하기
    for path in road:
        start, end, time = path
        graph[start].append((end, time))

    q = []

    def dijkstra(start):
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            time, now = heapq.heappop(q)
            if distance[now] < time:
                continue
            else:
                for route in graph[now]:
                    new_time = time + route[1]  # now -> route[0] 의 시간
                    if new_time < distance[route[0]]:
                        distance[route[0]] = new_time
                        heapq.heappush(q, (new_time,route[0]))

    dijkstra(1)
    cnt = 0
    print(distance)
    for i in distance:
        if i <= K:
            cnt += 1
    answer = cnt
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer
print(solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	,4))