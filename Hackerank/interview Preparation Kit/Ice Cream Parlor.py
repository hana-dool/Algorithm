def whatFlavors(cost, money):
    l = len(cost)
    st = set(cost)
    ans = []
    for i in st :
        less = money - i
        if less in st :
            ans = [i,less]
    rst = []
    for k in ans :
        t = cost.index(k)
        rst.append(t+1)
        cost[t] = -1
    rst.sort()
    print(*rst)
    return

whatFlavors([2,2,4,3],4)
