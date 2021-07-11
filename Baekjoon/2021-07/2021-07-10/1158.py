# N, K = map(int,input().strip().split())
# lst = list(range(1,N+1))
#
# def rotate(lst,k):
#     l = len(lst)
#     r = k % l
#     if r == 0 :
#         r = l
#     lst = list(lst[r:]) + lst[:r]
#     return(lst)
# ans = []
# l = lst
# while True :
#     l = rotate(l,K-1)
#     ans.append(l.pop(0))
#     if not l :
#         break
# print('<',end = '')
# print(', '.join(map(str,ans)),end = '')
# print('>')


## 다른 풀이
N, K = map(int,input().strip().split())
lst = list(range(1,N+1))
ans = []  # 제거된 사람들을 넣을 배열
idx = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    idx += K - 1
    if idx >= len(lst):  # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈
        idx = idx % len(lst)
    ans.append(lst.pop(idx))
print('<',end = '')
print(', '.join(map(str,ans)),end = '')
print('>')
