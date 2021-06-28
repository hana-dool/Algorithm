N = int(input())

start = [1,1]
lst = list(input().split())

for i in lst :
    if i == 'L' and 1 < start[1] :
        start[1] -= 1
    if i == 'R' and start[1] < N:
        start[1] += 1
    if i == 'U' and 1< start[0] :
        start[0] -= 1
    if i == 'D' and start[0]<N :
        start[0] += 1

print(start)