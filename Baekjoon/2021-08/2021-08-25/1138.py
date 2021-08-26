import sys
input = sys.stdin.readline
N = int(input())
line = [0]*N

lst = list(map(int,input().split()))

order = list(enumerate(lst))[::-1]
stack = []
for val, idx in order :
    stack.insert(idx,val+1)
print(*stack)