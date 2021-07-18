# N, S = map(int,input().split())
# lst = list(map(int,input().split()))
#
# # 합이 S 가 되게 하는것이 목표
# # Then gow to?
# # N <= 20 이기떄문에~ 완전 탐색이 가능하다 이말이야~
#
#
# # 01010101 로 선택과 미선택을 정해야하는데...
# # How to do?
# n = 2**N
#
# s = format(100,'b')
# ans = 0
# for i in range(n) :
#     cnt = 0
#     s = format(i,'b')
#     s = s.zfill(N)     # 01 00 10 11
#     lst_2 = list(map(int,list(s)))
#     for idx in range(N):
#         cnt += lst_2[idx] * lst[idx]
#     if cnt == S :
#         ans += 1
# if S == 0 :
#     print(ans-1)
# else :
#     print(ans)





## Note : DFS 를 이용한 탐색
N, S = map(int,input().split())
lst = list(map(int,input().split()))

# 합이 S 가 되게 하는것이 목표, N 이 리스트의 길이
# Then gow to?
# N <= 20 이기떄문에~ 완전 탐색이 가능하다 이말이야~

cnt = 0
def dfs(idx,sm) :
    global cnt
    if idx == N-1 :
        if sm and sum(sm) == S:
            cnt += 1
        return
    else :
        dfs(idx+1,sm+[lst[idx+1]])
        dfs(idx+1,sm)
dfs(0,[lst[0]])
dfs(0,[])
print(cnt)

