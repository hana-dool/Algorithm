import sys
input = sys.stdin.readline
N , M = map(int,input().split())
inf = 10** 9
mat = [[inf]*N for _ in range(N)]
for i in range(N) :
    mat[i][i] = 0
for _ in range(M) :
    person , friend = map(int,input().split())
    mat[person-1][friend-1] = 1
    mat[friend-1][person-1] = 1

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            mat[i][j] = min(mat[i][k]+mat[k][j],mat[i][j])
ans = []
for person in range(N) :
    cnt = 0
    for friend in range(N) :
        if mat[person][friend] == inf :
            continue
        else :
            cnt += mat[person][friend]
    ans.append(cnt)
print(ans.index(min(ans))+1)