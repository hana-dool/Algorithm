# https://www.acmicpc.net/problem/1541

# 55 - 50 + 40 + 40 - 30 + 40 - 40 - 40
# 55 - (50 + 40 + 40) - (30 + 40) - 40 - 40
# 즉 - 가 나오면, 그 뒤의 + 들은 다 괄호로 묶어주면 된다.

import sys
read = sys.stdin.readline
s = read()
lis = s.split('-')
val = eval(lis[0])
if len(lis) > 1 :
    for v in lis[1:] :
        val = eval(str(val) + '-' + '(' + v + ')')
print(val)

