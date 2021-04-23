# https://www.acmicpc.net/problem/1092
import sys
read = sys.stdin.readline
N = int(read()) # 크레인 수
lmt = list(map(int,read().split())) # 무게 제한
M = int(read()) # 박스의 수
wgt = list(map(int,read().split())) # wight 의 list



# 1. 우선 limit 와 weight 를 sort 한다.
# 8 4 2
# 7 5 4 2 2
lmt.sort(reverse = True) # 내림차순 정렬
wgt.sort(reverse = True) # 내림차순 정렬


#
# 3
# 5 4 1
# 10
# 5 5 4 3 3 2 1 1 1 1

if lmt[0] < wgt[0] :
    print(-1)
else:
    cnt = 0
    while wgt :
        for l in lmt:
            if not(wgt) :
                break
            elif l < wgt[-1]:
                continue
            else :
                for v in wgt :
                    if l >= v :
                        wgt.remove(v)
                        break
        cnt += 1
    print(cnt)
#
#
# if lmt[0] < wgt[0] :
#     print(-1)
# else :
#     cnt = 0
#     while wgt :
#         lmt_ = lmt.copy()
#         while lmt_ and wgt :
#             i = lmt_.pop()
#             for j in wgt :
#                 if i>= j : # 즉 제거할 수 있는상황
#                     wgt.remove(j)
#                     break
#         cnt += 1
# print(cnt)
#
#
#
#
#
#
