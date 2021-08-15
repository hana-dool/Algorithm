# import sys
# input = sys.stdin.readline
#
# N,S = map(int,input().split())
# lst = list(map(int,input().split()))
# start = 0
# end = -1
# val = 0
# l = 0
# ans = []
#
# # end 가 늘어나면서 체크
# def increase() :
#     global val,end,l
#     while end < N-1 : # val 이 S 와 같아지며ㅕㄴ 종료
#         if val + lst[end+1] >= S :
#             l += 1
#             ans.append(l)
#             end += 1
#             val += lst[end]
#             break
#         else :
#             l += 1
#             end += 1
#             val += lst[end]
#
# # start 가 늘어나면서 체크
# def decrease() :
#     global start,val,l
#     while True : # val 이 작아질거같으면 종료
#         if val - lst[start] >= S :
#             l -= 1
#             ans.append(l)
#             val -= lst[start]
#             start += 1
#         else :
#             break
#
# while True :
#     if end < N-1 :
#         increase()
#         decrease()
#     else :
#         break
# if ans :
#     print(min(ans))
# else :
#     print(0)


#--- 위 알고리즘은 너무 더럽다. 아래 알고리즘으로 다시.

import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
tmp_sum = 0
min_length = 10**9

while True:
    if tmp_sum >= S :
        min_length = min(min_length,right-left)
        tmp_sum -= arr[left]
        left += 1
    elif right == N :
        break
    else :
        tmp_sum += arr[right]
        right += 1
print(min_length)