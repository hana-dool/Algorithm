# import sys
# input = sys.stdin.readline
# N = int(input())
# lst = list(map(int,input().split()))
# positive = []
# negative = []
# for i in lst :
#     if i <0 :
#         negative.append(i)
#     else :
#         positive.append(i)
#
# positive = sorted(positive)
# negative = sorted(negative,reverse = True )
#
# if not positive :
#     print(negative[0], end =' ')
#     print(negative[1])
# if not negative :
#     print(positive[0], end =' ')
#     print(positive[1])
#
# n_idx = 0
# p_idx = 0
# mn = [10**12,0,0]
# while True :
#     # positive 고정 구간
#     if p_idx == len(positive) :
#         break
#     if n_idx <= len(negative) - 2:
#         if abs(positive[p_idx] + negative[n_idx+1]) > abs(positive[p_idx] + negative[n_idx]) :
#             # negative 가 커져봐야 의미 없다는것.. 즉 지금이 최소다!
#             mn = min(mn,[abs(positive[p_idx] + negative[n_idx]),negative[n_idx],positive[p_idx]],key = lambda x : x[0])
#             p_idx += 1
#         else :
#             # negative 가 커지니까 작아지긴한다.. 즉 가능성이 있어!
#                 n_idx += 1
#     elif n_idx == len(negative) - 1 :
#         mn = min(mn,[abs(positive[p_idx] + negative[n_idx]),negative[n_idx],positive[p_idx]],key = lambda x : x[0])
#         break
# print(mn[1], end = ' ')
# print(mn[2])


import sys
input = sys.stdin.readline
n = int(input())
lst = sorted(list(map(int, input().split())))

start = 0
end = len(lst) - 1
mn = [10**12,0,0]
while start < end :
    val = lst[end] + lst[start]
    mn = min([abs(val),lst[start],lst[end]],mn,key = lambda x : x[0])
    if val == 0  :
        print(lst[start],lst[end])
        break
    if val > 0 : # 너무 크니까 end 가 줄어라
        end -= 1
    if val < 0 :
        start += 1
print(*(mn[1],mn[2]))