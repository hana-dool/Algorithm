import sys
input = sys.stdin.readline

row , col = map(int,input().split())
N = int(input())
lst = []
for _ in range(N) :
    direction , place = map(int,input().split())
    lst.append([direction,place])
now_d , now_p = map(int,input().split())


def cal_diff(direct, place):
    # 같은 방향
    if now_d == direct :
        return abs(place-now_p)
    # 정반대 방향
    if (now_d,direct) in [(1,2),(2,1),(3,4),(4,3)] :
        # 오른쪽으로
        right = (row - now_p) + col + (row-place)
        # 왼쪽으로
        left = (now_p + col + place)
        return min(right,left)
    if (now_d,direct) in [(2,4),(4,2)] :
        return row + col - now_p - place
    if (now_d,direct) in [(2,3)] :
        return now_p + col - place
    if (now_d,direct) in [(3,2)] :
        return col - now_p + place
    if (now_d,direct) in [(1,3),(3,1)] :
        return now_p + place
    if (now_d,direct) in [(1,4)] :
        return place + row - now_p
    if (now_d,direct) in [(4,1)] :
        return now_p + row - place

sm = 0
for i in lst :
    x,y = i
    val = cal_diff(x,y)
    sm += val
print(sm)
        # 붙어있는 변

    # case 1 같은 방향
