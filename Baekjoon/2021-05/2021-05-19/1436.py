# https://www.acmicpc.net/problem/1436
import sys
read = sys.stdin.readline


gg = list(range(0,9999))
gg = [str(val).zfill(5) for val in gg]
rst = []
for i in gg :
    for idx in range(len(i)+1):
        lis = list(i)
        lis.insert(idx,'666')
        k = ''.join(lis)
        rr = int(k)
        rst.append(rr)

rst = list(set(rst))
rst.sort()
N = int(read())
print(rst[N-1])


# 666
# 1666
# 2666
# 3666
# 4666
# 5666
# 6660 6661 6662 6663 6664 6665 6667 6668 6669
# 7666
# 8666
# 9666
# 10666