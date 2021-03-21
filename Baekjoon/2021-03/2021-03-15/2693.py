import sys
read = sys.stdin.readline
T = int(read())

for _ in range(T):
    n = list(map(int,read().split()))
    n.sort()
    print(n[-3])
