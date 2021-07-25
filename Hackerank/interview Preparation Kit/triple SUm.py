def triplets(a, b, c):
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort(reverse =True)
    b.sort(reverse =True)
    c.sort(reverse =True)
    j = k = 0
    cnt = 0
    for i in range(len(b)) :
        while j < len(a) and k < len(c) :
            if a[j] > b[i] :
                j += 1
            if c[k] > b[i] :
                k += 1
            if a[j] <= b[i] and c[k] <= b[i] :
                print(a)
                print(b)
                print(c)
                print(j,i,k)
                print(f'{len(a[j:])} 와 {len(b[k:])}')
                cnt += len(a[j:]) * len(c[k:])
                break
    return cnt
print(triplets([1,4,5],[2,3,3],[1,2,3]))



