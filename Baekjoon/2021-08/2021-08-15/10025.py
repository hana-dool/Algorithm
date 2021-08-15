import sys
input = sys.stdin.readline

arr = [0] * 1000001

N, K = map(int, input().split())
for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g

step = K * 2 + 1
tmp = sum(arr[:step])
result = tmp

for i in range(step, 1000001):
    tmp += arr[i] - arr[i-step]
    result = max(result, tmp)
print(result)