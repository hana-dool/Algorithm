import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
s_lst = sorted(list(set(lst)))
dic = dict(zip(s_lst,list(range(len(s_lst)))))
for i in lst:
    print(dic[i],end=' ')
