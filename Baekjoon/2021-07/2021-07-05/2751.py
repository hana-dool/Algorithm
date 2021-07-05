import sys
read = sys.stdin.readline

n = int(read().strip())

lst = []

for _ in range(n):
    lst.append(int(read()))
lst.sort()
for i in lst :
    print(i)