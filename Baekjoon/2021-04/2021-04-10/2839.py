#---------내 코드-----------#
import sys
read = sys.stdin.readline
# 3kg / 5kg...

N = int(read())
# 5/3
k = N // 5
r = N % 5

gg = 0
while True :
    if k < 0 :
        gg = 1 # 아 끝낫다.. 이건 불가능!
        break
    elif r % 3 == 0 : # 3의 배수긴 허네..
        y = r//3
        cnt = k + y
        break
    else :
        r += 5
        k -= 1

if gg == 1 :
    print(-1)
else :
    print(cnt)




# 다른사람 코드리뷰
total = int(input())
bag = 0
while total % 5:
    total -= 3
    bag += 1
print(-1 if total<0 else total // 5 + bag)