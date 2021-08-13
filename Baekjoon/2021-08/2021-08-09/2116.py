import sys
import copy
input = sys.stdin.readline

T = int(input())
cube_raw = []
for _ in range(T) :
    lst = list(map(int,input().split()))
    graph = dict()
    graph[lst[0]] = lst[5]
    graph[lst[5]] = lst[0]
    graph[lst[1]] = lst[3]
    graph[lst[3]] = lst[1]
    graph[lst[2]] = lst[4]
    graph[lst[4]] = lst[2]
    cube_raw.append(graph)

ans = []
for start in range(1,7):
    cnt = 0
    s = start
    cube = copy.deepcopy(cube_raw)
    while cube :
        cubic = cube.pop(0)
        s = cubic[s]
        mx = []
        for plain in cubic.items() :
            if plain[0] == s or plain[1] == s :
                pass
            else :
                mx.append(plain[1])
        cnt += max(mx)
    ans.append(cnt)
print(max(ans))





