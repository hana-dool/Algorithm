def countTriplets(arr, r):
    dic = {}
    for i in arr :
        dic[i] = dic.get(i,0) + 1
    cnt = 0
    if r == 1 :
        for k in dic.values() :
            cnt += k *(k-1) * (k-2) // 6
        return(cnt)
    for j in arr : # 중간값 순회
        if j % r == 0 :
            cnt += dic.get(j//r,0) * dic.get(j * r,0)
    return(cnt)

100 * 99 * 98 / 6


print(countTriplets([1,1,1,1,1,1,1,1,1,1], 1))