import sys
read = sys.stdin.readline

N = int(read())
lis1 = list(map(int , read().split()))
lis2 = list(map(int , read().split()))

lis1.sort()
lis2.sort(reverse = True)

sum = 0
for i in zip(lis1,lis2) :
    sum += i[0] * i[1]

print(sum)