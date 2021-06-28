n,m = map(int,input().split())

mat = [list(map(int,input().split())) for _ in range(n)]
mx = 0

for y in range(n):
    lst = mat[y]
    if min(lst) > mx :
        mx = min(lst)
print(mx)
