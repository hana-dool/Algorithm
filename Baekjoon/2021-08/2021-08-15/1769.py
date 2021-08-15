import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

val = input().rstrip()
cnt = 0
while True :
    if len(str(val)) == 1 :
        break
    else :
        cnt += 1
        val = sum(map(int,list(str(val))))
print(cnt)
if int(val) % 3 == 0 :
    print('YES')
else :
    print('NO')

# def recur(val,cnt) :
#     if len(str(val)) == 1 :
#         return val,cnt
#     sm = sum(map(int,list(str(val))))
#     return recur(sm,cnt + 1)
# v,ans = recur(val,0)
# print(ans)
# if v % 3 == 0 :
#     print('YES')
# else :
#     print('NO')