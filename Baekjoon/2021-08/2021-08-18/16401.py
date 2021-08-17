import sys
input = sys.stdin.readline

M,N = map(int,input().split())

lst = list(map(int,input().split()))
def count_maximum(x) :
    cnt = 0
    for i in lst :
        cnt += i//x
    return cnt
start = 1
end = max(lst)

while start <= end :
    mid = (start + end) // 2
    if count_maximum(mid) == M :
        start = mid + 1
    elif count_maximum(mid) > M : # 너무 많이 쪼갯다. 좀 더 커져도 될듯
        start = mid + 1
    elif count_maximum(mid) < M :
        end = mid - 1 # 너무 조금 쪼갰다. 작아지자.
print(end)

