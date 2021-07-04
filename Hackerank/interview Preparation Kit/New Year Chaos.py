# 아래는, 하나 구할때마나 mx 구하고. idx 구하는게 오바라는듯..
def minimumBribes(q):
    lst = q
    tot = 0
    while lst :
        mx = max(lst)
        idx = lst.index(mx)
        if len(lst) - 3 > idx :
            print('Too chaotic')
            return
        else :
            # max 값을 없앤다.
            tot += (len(lst) -1 - idx)
            lst.remove(mx)
    print(tot)

# 아래의 경우가 훨씬 시간이 적게든다..
# 경이롭네요..
def minimumBribes(q):
    i = 0
    dic = {}
    while i < len(q)-1 :
        if q[i] > q[i+1] :
            dic[q[i]] = dic.get(q[i],0) + 1
            if dic[q[i]] > 2 :
                print('Too chaotic')
                return
            q[i],q[i+1] = q[i+1],q[i]
            if i != 0:
                i -= 1
        else :
            i += 1
    print(sum(dic.values()))

minimumBribes([2,1,5,3,4])
