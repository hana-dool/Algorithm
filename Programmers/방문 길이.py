from collections import deque


def solution(dirs):
    mat = [[0] * 11 for _ in range(11)]
    # current = 5,5
    # 무조건 bfs! 
    x, y = 5, 5
    d = deque(list(dirs))
    # 진짜 맞게 만들려면... 아래와 같이 매핑해야한다.
    mapping = {'U': [0, -1], "R": [1, 0], "D": [0, 1], "L": [-1, 0]}

    ans = set()
    while d:
        temp = d.popleft()
        direction = mapping[temp]
        nx = x + direction[1]  # x가 세로이다.
        ny = y + direction[0]  # y가 가로이다.
        if 0 <= nx < 11 and 0 <= ny < 11:
            lis = [(x, y), (nx, ny)]
            lis = tuple(sorted(lis, key=lambda x: (x[0], x[1])))
            ans.add(lis)
            x = nx
            y = ny
    answer = len(ans)
    print(ans)
    return answer