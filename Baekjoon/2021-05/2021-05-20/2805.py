import sys
read = sys.stdin.readline

N,M = map(int,read().split())
lst = list(map(int,read().split()))


def cal(x):
    val = 0
    for i in lst:
        if i-x > 0:
            val += (i-x)
    return(val)

# M 이 우리의 기준이 된다.

start = 1
end = max(lst)

while start <= end : # 이 경우.. 5 6 9 9 9 10 .. 인 경우 처음을 출력해야
    mid = (start + end)//2
    val = cal(mid)
    if M == val :
        start = mid + 1 # 같은 경우 start 가 올라가는게 핵심
    elif M < val : #val이 크다? 그건 mid 가 너무 작아서그럼
        start = mid + 1
    elif M > val : # val이 작다? 그건 mid 가 너무 커서 그럼
        end = mid - 1
print(end) # start 가 선 넘었을때 중지되므로 end 가 정석값