import sys
read = sys.stdin.readline
N = int(read())
lis = [1]
for _ in range(1,60):
    lis.append(lis[-1] + _)

for i in range(len(lis)-1):
    if lis[i] <= N and lis[i+1] > N :
        k = N - lis[i]
        a = i + 1 - k
        b = 1 + k
        break

print(a,b)
