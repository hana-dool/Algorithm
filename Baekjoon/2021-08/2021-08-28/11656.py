import sys
input = sys.stdin.readline
S = input().strip()
l = len(S)
lst = []
for i in range(l) :
    lst.append(S[i:])
lst = sorted(lst)
for i in lst :
    print(i)