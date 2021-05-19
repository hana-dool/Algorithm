import sys
read = sys.stdin.readline
N,M = map(int,read().split())
lst = [int(read()) for _ in range(N)]
lst.sort()

# lst 를 받았을때에, 인접한 거리가 3 이상이 되게
def _cnt(x):
    stk = [lst[0]]
    for i in lst :
        if i - stk[-1] >= x :
            stk.append(i)
    return(len(stk))

# 공유기를 M 개 설치하려 한다.

start = 1 # 최소 거리
end = max(lst) # 최대 거리
while start <= end :
    mid = (start + end)//2
    val = _cnt(mid)
    if val == M : # 공유기 갯수가 M 이야! 하지만 거리를 늘리고싶어
        start = mid + 1
    elif val > M : # 공유기 갯수가 M 보다 커! 그럼 거리를 늘리자.
        start = mid + 1
    elif val < M : # 공유기 갯수가 M 보다 작아! 그럼 거리를 줄이자.
        end = mid - 1
# 2 3 3
print(end) #