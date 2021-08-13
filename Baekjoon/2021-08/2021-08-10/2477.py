N = int(input())
lst = [list(map(int,input().split())) for _ in range(6)]
lst = lst + lst
l = len(lst)

for i in range(l-1) :
    if lst[i][0] == lst[i+2][0] and lst[i+1][0] == lst[i+3][0] :
        temp = lst[i:i+6]
        break
ans = temp[4][1]*temp[5][1] - temp[1][1]*temp[2][1]
print(ans*N)