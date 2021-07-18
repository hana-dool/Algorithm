from collections import deque
def solution(arr):
    arr = deque(arr)
    ans = [-1]
    while arr :
        val = arr.popleft()
        if ans[-1] != val : # 다른경우에만 넣자~
            ans.append(val)
    answer = ans[1:]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer