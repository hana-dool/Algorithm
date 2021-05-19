import sys
read = sys.stdin.readline

N,M = map(int,read().split())
# M : 필요한 전선의 수

# 9 8 8 7 6 5 5 5 4 4

lst = [ int(read()) for _ in range(N)]

start = 1
end = sum(lst) // M

def cnt(x):
    val = 0
    for i in lst:
        val += i // x
    return(val)
# cnt 에 의해 계산되는 값은 내림차순을 따르게 된다.

while start <= end  : # start 가 선 넘을떄
    mid = (start + end) // 2
    val = cnt(mid)
    if val == M :
        start = mid + 1  # 같은 경우여도 커지는것이 핵심
    elif val > M : # 우리가 찾고자 하는 값이 너무 작다.
        start = mid + 1
    elif val < M : # 우리가 찾고자 하는 값이 너무 크다.
        end = mid - 1
print(end) # end 출력하자.



