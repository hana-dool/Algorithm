N, M = map(int,input().split())
lst = list(map(int,input().split()))
import bisect

def cal_length(height,lst) :
    cnt = 0
    for tree in lst :
        if height < tree :
            cnt += (tree - height)
    return cnt

# cal_length 는, height 가 커질수록 작아지는 함수입니다.
# 우리가 찾고싶은것은 주어진 조건을 만족하되,

start = min(lst)
end = max(lst)

# 37이 답이라 하자.
# 38 37 37 37 36 이 경우 답은 맨 뒤의것 (upper bound)
# 1 2 3 4 5 6 ...
# 54 49 45 42 41 40 40 35


while start <= end :
    mid = (start + end) // 2
    if cal_length(mid,lst) == M :
        start = mid + 1
    elif cal_length(mid,lst) > M : # 너무 크면 줄여야됨
        end = mid - 1
    elif cal_length(mid,lst) < M : # 너무 작으면 커져야된
        start = mid + 1
print(end) # start 는 존재하지 않으면 뒤의것 출력

