def luckBalance(k, contests):
    ans = 0
    contests = sorted(contests,key = lambda x : (x[1],x[0]),reverse=True)
    for i in contests:
        if i[1] == 0 :
           ans += i[0]
    for i in contests:
        if i[1] == 1 :
            if k <= 0 :
                ans -= i[0]
            else :
                k -= 1
                ans += i[0]
    return(ans)
luckBalance(3,[[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])


