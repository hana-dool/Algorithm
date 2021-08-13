import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    name,hangul,eng,math= list(input().split())
    hangul = int(hangul)
    eng = int(eng)
    math = int(math)
    lst.append([name,hangul,eng,math])
s_lst = sorted(lst, key= lambda x : (-1*x[1],x[2],-1*x[3],x[0]))
for i in s_lst :
    print(i[0])

