def maximumToys(prices, k):
    prices.sort()
    m = 0
    cnt = 0
    for v in prices :
        if m + v > k : # over bedget
            break
        else :
            m += v
            cnt += 1
    return(cnt)

