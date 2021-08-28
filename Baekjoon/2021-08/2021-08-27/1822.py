import sys
input = sys.stdin.readline
n_A , n_B = map(int,input().split())
A_set = set(map(int,input().split()))
B_set = set(map(int,input().split()))

cnt = 0
ans = []
for element in A_set :
    if element in B_set :
        continue
    else :
        cnt += 1
        ans.append(element)
print(cnt)
ans.sort()
if ans :
    print(*ans)