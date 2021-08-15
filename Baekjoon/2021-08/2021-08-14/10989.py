import sys
input = sys.stdin.readline
N = int(input())
lst = [0]*10001

for _ in range(N):
    val = int(input())
    lst[val] += 1
for i in range(1,10001) :
    if lst[i] != 0 :
        for _ in range(lst[i]) :
            print(i)
