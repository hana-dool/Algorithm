import sys
read = sys.stdin.readline

def P(N):
    lis = [0, 1, 1, 1, 2, 2]
    if N <= 5 :
        print(lis[N])
    else :
        for _ in range(N-5):
            lis.append(lis[-1]+lis[-5])
        print(lis[-1])
T = int(read())
for _ in range(T):
    P(int(read()))