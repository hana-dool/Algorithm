# https://www.acmicpc.net/problem/1541

# 55 - 50 + 40 + 40 - 30 + 40 - 40 - 40
# 55 - (50 + 40 + 40) - (30 + 40) - 40 - 40
# 즉 - 가 나오면, 그 뒤의 + 들은 다 괄호로 묶어주면 된다.

import sys
read = sys.stdin.readline
s = read()
lis = s.split('-')
# 바로 eval 을 쓰게되면.. 안되네? 04 이런거떄문에
lis2 = []
for l in lis :
    lis2.append(list(map(int,l.split('+'))))

val = sum(lis2[0])
if len(lis2) > 1 :
    for v in lis2[1:] :
        val -= sum(v)
print(val)


#---------- 다른 사람 코드
n = [sum(int(x) for x in y.split('+')) for y in input().split('-')]
print(n[0] - sum(n[1:]))
# 훨씬 간결하고, list comprehension 을 적극 이용한 점이 인상깊다.