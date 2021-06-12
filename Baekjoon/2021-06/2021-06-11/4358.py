import sys
read = sys.stdin.readline
dic = {}
tot = 0
while True :
    tree = read().strip()
    if not tree :
        break
    dic[tree] = dic.get(tree,0) + 1
    tot += 1
lst = sorted(dic.items())
print(lst)
for i,v in lst:
    print(f'{i} {round(100*v/tot,4)}')


