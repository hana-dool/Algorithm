# https://www.acmicpc.net/problem/2217
import sys
read = sys.stdin.readline
N = int(read())

rope = []
for _ in range(N):
    rope.append(int(read()))

rope.sort(reverse=True)

max = 0
for i,val in enumerate(rope):
    k = val * (i+1)
    if k > max :
        max = k
print(max)


#---