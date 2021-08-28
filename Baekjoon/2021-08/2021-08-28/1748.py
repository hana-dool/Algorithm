import sys
input = sys.stdin.readline
N = input().strip()
l = len(N)
mapping = [9 * (10**i) for i in range(10)]
cnt = 0
for i in range(l-1) :
    cnt += mapping[i] * (i+1)
if len(N) == 1 :
    print(int(N)*1)
else :
    cnt += (int(N)+1 - int(10**(len(N)-1)) )*len(N)
    print(cnt)
