N = int(input())
mat = [list(input()) for _ in range(N)]


fr = [set() for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if mat[i][j] == 'Y' :
            fr[i].add(j) # 1단계 친구
        for k in range(N) :
            if mat[i][j] == 'Y' and mat[j][k] == 'Y' :
                fr[i].add(k)
for i,v in enumerate(fr) :
    v.discard(i)
print(max(list(map(len,fr))))

