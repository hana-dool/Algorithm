import sys
input = sys.stdin.readline
N = int(input())
dp_right = [0]*N
dp_left = [0]* N
dp_all = [0]*N


dp_right[0] = 1
dp_left[0] = 1
dp_all[0] = 1

for i in range(1,N) :
    dp_all[i] = (dp_left[i-1] + dp_right[i-1] + dp_all[i-1])%9901
    dp_right[i] = (dp_left[i-1] + dp_all[i-1])%9901
    dp_left[i] = (dp_right[i-1] + dp_all[i-1])%9901

print((dp_all[-1] + dp_right[-1] + dp_left[-1]) % 9901 )
