from collections import deque
ans = 0
def solution(numbers, target):
    l = len(numbers)
    def dfs(depth,cnt) :
        global ans
        if depth == l :
            if cnt == target :
                ans += 1
        else :
            dfs(depth + 1 , cnt - numbers[depth])
            dfs(depth + 1 , cnt + numbers[depth])
    dfs(0,0)
    answer = ans
    return answer

print(solution([1,1,1,1,1],3))