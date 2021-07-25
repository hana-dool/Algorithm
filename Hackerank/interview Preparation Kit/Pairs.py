def pairs(k, arr):
    st = set(arr)
    cnt = 0
    for i in st :
        if k-i in st :
            cnt += 1
    return cnt // 2 