name = input()
l = len(name)
from collections import defaultdict
import sys
dic = defaultdict(int)
for i in name :
    dic[i] += 1

lst = sorted(list(map(list,dic.items())),key= lambda x : x[0] )
def check() :
    if l % 2 == 0 :
        for i in lst :
            if i[1] % 2 != 0 :
                print("I'm Sorry Hansoo")
                return
    else :
        cnt = 0
        for i in lst :
            if i[1] % 2 != 0 :
                cnt += 1
        if cnt > 1 :
            print("I'm Sorry Hansoo")
            return
    ans = ''
    kit = ''
    rst = ''
    for i in lst :
        while i[1]>=2 :
            ans += i[0]
            i[1] -= 2
        if i[1] == 1 :
            kit += i[0]
    rst = ans+kit+ans[::-1]

    print(rst)
check()



