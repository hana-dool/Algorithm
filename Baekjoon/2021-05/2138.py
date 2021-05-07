# https://www.acmicpc.net/problem/2138
import sys
read = sys.stdin.readline
# N = 10만, 2(2억)초 이므로
# N*logN 까지는 허용가능

# 앞에서부터 Greedy 하게 하면 될 듯 하다.

# -**-*-* 0000000 # 같고 다름을 -와 *로 표현
# ---**-* 0111000
# -----** 0110110
# ------- 0110101

T = int(read())
lst1 = list(read())
lst2 = list(read())

lst = []
for i in range(T):
    lst.append(int(lst1[i] != lst2[i])) # 같으면 0, 다르면 1

#    010
#[1] 100 010
#[2] 100 011 101 010 -- 011, 010 만 살아남음
#[3] 011 000 010 001 # 000 이 나왔으므로 끝.

# 그러면 대체 어떻게 해야됨 ?

def change1(x):
    x[0] = abs(x[0] - 1)
    x[1] = abs(x[0] - 1)
    return(x)

def change2(x,i) :
    x[i-1] = abs(x[i-1] - 1)
    x[i] = abs(x[i] - 1)
    x[i+1] = abs(x[i+1] - 1)
    return(x)

def change3(x):
    x[-1] = abs(x[-1] - 1)
    x[-2] = abs(x[-2] - 1)
    return(x)

ans = [lst]
for i in range(len(lst)) :
    lis = []
    if i == 0 :
        for j in ans :
            lis.append(change1(j))
            lis.append(j)
    elif i == len(lst) - 1 :
        for j in ans :
            lis.append(change3(j))
            lis.append(j)
    else :
        for j in ans :
            lis.append(change2(j,i))
            lis.append(j)
    if i != 0 :
        for k in range(len(lis)) :
            if lis[k][i-1] != 0:
                lis.pop(k)
    for val in lis :
        if sum(val) == 0 :
            print(i)
    ans = lis




