import sys
read = sys.stdin.readline
N = int(read())
lis = list(map(int,read().split()))
lis.sort() # N명
weight = list(range(N,0,-1)) # N ~ 1  의 가중치 선정
cnt = 0
for i in range(N):
    val = lis[i] * weight[i]
    cnt += val

print(cnt)
