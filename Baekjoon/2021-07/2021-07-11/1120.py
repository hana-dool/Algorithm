# A <= B
A,B = input().strip().split()


def ch(x,y):
    cnt = 0
    l = len(x)
    for i in range(l):
        if x[i] != y[i] :
            cnt += 1
    return cnt

diff = len(B) - len(A)
ans = []
for i in range(diff+1): # 0 ~ diff
    j = diff - i
    new_A = B[:i] + A + B[len(B)-j:]
    ans.append(ch(new_A,B))
print(min(ans))
