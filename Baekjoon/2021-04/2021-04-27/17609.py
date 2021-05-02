# # https://www.acmicpc.net/problem/17609
# import sys
#
# read = sys.stdin.readline
# T = int(read())
# #--- 시간 초과 ---
# for _ in range(T) :
#     r = 0
#     st = read() # string 으로 받기
#     st = st.strip()
#     st = list(st)
#     ch = 0
#     while True : # st 가 빌때까지
#         if len(st) > 1 :
#             if st[0] == st[-1] :
#                 st.pop()
#                 st.pop(0)
#             else :
#                 if st[0] == st[-2] and ch == 0 : # 145412
#                     ch += 1
#                     st.pop()
#                 elif st[1] == st[-1] and ch == 0 :# 124542
#                     ch += 1
#                     st.pop(0)
#                 else :
#                     print(2)
#                     break # while 끝내기 # 1432624
#         else :
#             if ch >= 1:
#                 print(1)
#                 break
#             else :
#                 print(0)
#                 break
#
#
#
# i 번째가 다를때에, 얘가 회문인지를 추가적으로 판단하게 해주는 함수가필요
def left_check(w,i): # i 를 뺸 상태에서 같은지 아닌지 검사
    t = w.copy()
    t.pop(i)
    if t == t[::-1] :
        return(1)

def right_check(w,i):
    t = w.copy()
    t.pop(-1-i)
    if t == t[::-1]:
        return(1)

import sys
read = sys.stdin.readline
T = int(read())
for _ in range(T):
    w = list(read().strip())
    for i in range(len(w)//2):
        if w[i] != w[-1-i] :
            if left_check(w,i) :
                print(1)
                break
            elif right_check(w,i) :
                print(1)
                break
            else :
                print(2)
                break
    else :
        print(0)