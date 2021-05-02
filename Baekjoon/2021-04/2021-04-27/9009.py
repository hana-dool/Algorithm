# https://www.acmicpc.net/problem/9009

import sys
read = sys.stdin.readline

lmt = 1000000000
lst = [1,1]
x = 0

# 먼저 리스트 만들기
while True :
    if lst[-1] > lmt :
        break
    else :
        lst.append(lst[-1]+lst[-2])
lst.reverse()

# 큰거부터 출력하기
N = int(read())
for _ in range(N):
    val = int(read())
    ans = []
    for i in lst :
        if i <= val :
            val -= i
            ans.append(i)
    ans.reverse()
    for x in ans :
        print(x, end = ' ')
    print()

# 이건 솔직히 수학적으로 '왜 최소인가?' 를 밝히는것이 훨씬 중요하다고 생각합니다.
# 자기와 제일 근접한 값을 선택하지 않는다면,(144라 합시다.) 55,89 를 같이 선택할 수 없습니다.
# 이 상태에서 최대값은 89 34 13 5.. 인데, (인접한거 고르는것은, 최소 숫자를 고른다는 원칙에 위배)
# 하나씩 띄어서 고르는것은, 144보다 작아짐
# 144 -? 89 55 -> 89 34 21 -> 89 34 13 8 ....
