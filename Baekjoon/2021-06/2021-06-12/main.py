# N  = int(input())
# ch = [0] * N
#
# def DFS(x):
#     if x >= N :
#         for i in range(N):
#             if ch[i] ==1 :
#                 print(i+1, end=' ')
#         print()
#     else :
#         ch[x] = 1
#         DFS(x+1)
#         ch[x] = 0
#         DFS(x+1)
# DFS(0)
#
#
#
# ###
#
# import sys
# N = int(input())
# lst = list(map(int,input().split()))
#
# cnt = 0
# ans = sum(lst)
# done = 0
#
# def DFS(x):
#     global cnt
#     global ans
#     if cnt == ans/2 :
#         print('YES')
#         done = 1
#         sys.exit(0)
#     if x >= N :
#         return
#     else :
#         cnt += lst[x]
#         DFS(x+1)
#         cnt -= lst[x]
#         DFS(x+1)
# DFS(0)
# if done == 0 :
#     print('NO')




import sys

N = int(input())
lst = list(map(int,input().split()))
tot = sum(lst)
def DFS(L,sum):
    if L == N :
        if sum == tot-sum:
            print("YES")
            sys.exit(0)
    else :
        DFS(L+1,sum + lst[L])
        DFS(L+1,sum)
DFS(0,0)
print('NO')

