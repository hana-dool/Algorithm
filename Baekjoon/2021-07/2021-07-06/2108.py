import sys
input = sys.stdin.readline
n = int(input())
lst = [ ]
for _ in range(n):
    lst.append(int(input()))
lst.sort()
length = len(lst)
mean_ = round(sum(lst) / length)
median_ = lst[(length-1)//2]
dic = {}
for i in lst:
    dic[i] = dic.get(i,0) + 1
dic_sorted = sorted(dic.items(),key = lambda x : x[1],reverse = True)
if length == 1 :
    freq_ = dic_sorted[0][0]
elif dic_sorted[0][1] == dic_sorted[1][1]:
    freq_ = dic_sorted[1][0]
else :
    freq_  = dic_sorted[0][0]
range_ = lst[-1] - lst[0]

print(mean_)
print(median_)
print(freq_)
print(range_)