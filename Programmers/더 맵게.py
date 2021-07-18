import heapq

def solution(scoville, K):
    q = scoville
    heapq.heapify(q)
    cnt = 0
    while q[0] < K:
        if len(q) == 1:
            return -1
        a_1 = heapq.heappop(q)
        a_2 = heapq.heappop(q)
        a_n = a_1 + a_2 * 2
        heapq.heappush(q, a_n)
        cnt += 1

    answer = cnt
    return answer

