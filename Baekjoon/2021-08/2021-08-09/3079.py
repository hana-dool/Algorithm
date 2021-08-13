import sys
input = sys.stdin.readline
N,M = map(int,input().split())
lst = []
for _ in range(N) :
    lst.append(int(input()))

# 시간에 따른, 사람이 몇명 가능한가?
def cal_people(x) :
    cnt = 0
    for i in lst :
        cnt += x//i
    return cnt

start = 0
end = 10**20
while start <= end :
    mid = (start+end)//2
    if cal_people(mid) == M  : # 지금 시간이 딱 맞음!
        end = mid -1  # 더 작아지고파
    elif cal_people(mid) > M : # 사람이 많다? 시간이 작아져도 좋다.
        end = mid - 1
    elif cal_people(mid) < M :
        start = mid + 1
print(start)
