import sys
input = sys.stdin.readline

n,m = map(int,input().strip().split())
set_1 = set()
set_2 = set()
for _ in range(n):
    set_1.add(input().strip())
for _ in range(m):
    set_2.add(input().strip())
ans = []
for people in set_1 :
    if people in set_2 :
        ans.append(people)
ans.sort()
print(len(ans))
for i in ans :
    print(i)



a = [1,2,3]
b = a

b[0] = 4
a