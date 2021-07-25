import sys
input = sys.stdin.readline
N = input()
lst = list(N)
dic = {}
for i in lst :
    if i == '6' or i == '9' :
        dic['6'] = dic.get('6',0) + 1
    else :
        dic[i] = dic.get(i,0) + 1
dic['6'] = dic.get('6',0) // 2 + dic.get('6',0) % 2
print(max(dic.values()))