from collections import deque


def solution(prices):
    l = len(prices)
    order = list(range(l))
    price_order = list(map(list, zip(prices, order)))
    price_order = deque(price_order)
    stack = []
    ans = [0] * l
    while len(price_order) > 1 :
        p = price_order.popleft()
        if stack:  # 스택에 들어있음
            while stack and stack[-1][0] > p[0]:
                stack.pop()
            stack.append(p)
        else:
            stack.append(p)
        for element in stack:
            ans[element[1]] += 1
    answer = ans
    return answer

print(solution([2,1,5,1,3]))