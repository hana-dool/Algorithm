N, K = map(int,input().split())

M_hash = [0]*7
W_hash = [0]*7
for _ in range(N):
    S,Y = map(int,input().split())
    if S == 0 :
        W_hash[Y] += 1
    else :
        M_hash[Y] += 1
cnt = 0
for i in M_hash :
    if i == 0 :
        continue
    elif i % K == 0 :
        cnt += (i // K)
    else :
        cnt += (i // K) + 1
for i in W_hash :
    if i == 0 :
        continue
    elif i % K == 0:
        cnt += (i // K)
    else:
        cnt += (i // K) + 1
print(cnt)

