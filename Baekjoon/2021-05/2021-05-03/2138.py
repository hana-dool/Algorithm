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

def change1(x): # 처음꺼 2개 바꿈
    a = x.copy()
    a[0] = abs(x[0] - 1)
    a[1] = abs(x[1] - 1)
    return(a)

def change2(x,i) : # 3개 바꿈
    a = x.copy()
    a[i-1] = abs(x[i-1] - 1)
    a[i] = abs(x[i] - 1)
    a[i+1] = abs(x[i+1] - 1)
    return(a)

def change3(x): # 2개 바꿈
    a = x.copy()
    a[-1] = abs(x[-1] - 1)
    a[-2] = abs(x[-2] - 1)
    return(a)
4
0000
1111

ans = [lst]
cnt = 0
length = len(lst)
gg = 0
dic = {lst : 0}
for i in range(length) :
    lis = [] # emplty 한 list 를 만듦
    if i == 0 :
        for j in ans : # ans 에 대해서
            lis.append(change1(j))  # 한번 바꾼것도 append
            lis.append(j) # 원래 존재했던 값도 append
    elif i == length - 1 :
        for j in ans :
            lis.append(change3(j))
            lis.append(j)
    else :
        for j in ans :
            lis.append(change2(j,i))
            lis.append(j)
    print(f'쌓이는 리스트 : {lis}')
    # 010
    # 100 010
    # 100 010 011 101
    # 000
    # 위의 과정은 lis 에 우리의 연산들을 모두 append 한 과정

    # 이제 , 우리의 연산으로 생성된 lis 에 대해서
    if i != 0 :
        l = len(lis)
        empty = []
        for k in range(l) :
            if lis[k][i-1] == 0:
                # lis 내의 원소에 대해, i-1 번쨰가 0이라면 잘 된것들이므로 얘네만 필요
                empty.append(lis[k]) # 잘 된애들
        lis = empty # 잘 된애들을 lis 에넣어줌
    cnt += 1
    for val in lis : # 만약 그 값들중에서
        if sum(val) == 0 : # sum 이 0 인 애가있으면 다 완료된것
            print(cnt)
            gg = 1
            break
    if gg == 1:
        break
    # 이제 lis 에 잘 된 애들만 남아있음
    ans = lis
