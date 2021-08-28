from collections import defaultdict

N = int(input())
dic = defaultdict(int)
for _ in range(N):
    val = int(input())
    dic[val] += 1
dic = dict(dic)
sorted_lst = sorted(dic.items(),key =lambda x : (-x[1],x[0]))
print(sorted_lst[0][0])
