N,K,B = map(int,input().split())
road = [0]*N
for _ in range(B) :
    a = int(input())
    road[a-1] = 1
init = sum(road[:K])
mn = init
for i in range(K, N) :
    init += road[i]-road[i-K]
    mn = min(init,mn)
print(mn)
# 연속한 K 개 존재하도록
