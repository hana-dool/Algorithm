N = int(input())
dic = {}
for _ in range(N) :
    book = input()
    dic[book] = dic.get(book,0) + 1
lst = sorted(dic.items(),key = lambda x : (x[1],x[0]), reverse = True)
mx = lst[0][1]
print([i for i,v in lst if v == mx][-1])
