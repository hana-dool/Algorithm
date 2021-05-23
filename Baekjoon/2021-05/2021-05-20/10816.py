import sys
read = sys.stdin.readline

N = int(read())
lst1 = list(map(int,read().split()))
M = int(read())
lst2 = list(map(int,read().split()))

# ---- 이진탐색은 쓰레기인거같아..------ #

# lst1.sort()
#
# # lst1 에 있는지 없는지를 검사...
# ans = {}
# dic = {}
# for i in lst2 :
#     if i not in dic:
#         start = 0
#         end = len(lst1)-1
#         cnt = 0
#         while start <= end :
#             mid = (start + end) // 2
#             if lst1[mid] == i :
#                 cnt = lst1[start:end+1].count(i)
#                 break
#             elif lst1[mid] < i :
#                 start = mid + 1
#             elif lst1[mid] > i :
#                 end = mid - 1
#         dic[i] = cnt
#     # end 가 끝난지점
# for v in lst2 :
#     print(dic[v],end = ' ')


dic = {}
for n in lst1:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
for v in lst2 :
    if v in dic :
        print(dic[v],end = ' ')
    else :
        print(0, end = ' ')
