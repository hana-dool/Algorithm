import sys
read = sys.stdin.readline

n,m = map(int,input().split())
mat = [list(map(int,list(read().strip()))) for _ in range(n)]

ans = [0]
for a in range(1,min(n,m)):
    dx = [a, 0, a]
    dy = [0, a, a]
    ch = 0
    for i in range(n):
        if ch == 1 :
            break
        for j in range(m):
            val = mat[i][j]
            for d in range(3):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < m and val == mat[nx][ny]:
                    continue
                else : # 중간에 마주치면 파토낸다.
                    break
            else : # 다 잘 통과했어야! 이거 들어온다.
                ans.append(a)
                ch = 1
                break
t = max(ans)
print((t+1)**2)



