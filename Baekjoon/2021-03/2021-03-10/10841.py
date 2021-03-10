# https://www.acmicpc.net/problem/10814
import sys
read = sys.stdin.readline
N = int(read())
val = []
for _ in range(N):
    a,b = read().split()
    a = int(a)
    val.append([a,b])
val.sort( key = lambda x : x[0])
for i in val :
    print(i[0],end = ' ')
    print(i[1])