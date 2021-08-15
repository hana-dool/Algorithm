# import sys
# input = sys.stdin.readline
#
#
# N = int(input())
# dp = [1]* N
# lst = list(map(int,input().split()))
#
# for end in range(N):
#     for search in range(end):
#         if lst[search] < lst[end] :
#             dp[end] = max(dp[end],dp[search]+1)
# print(max(dp))


import sys
input = sys.stdin.readline
N = int(input())

lst=  list(map(int,input().split()))
dp = lst.copy()
for end in range(N) :
    for search in range(end) :
        if lst[search] < lst[end] :
            dp[end] = max(lst[end]+dp[search], dp[end])
print(max(dp))