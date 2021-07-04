def countSwaps(a):
    cnt = 0
    for i in range(len(a)-1,0,-1) : # 끝점의 기준
        for j in range(i): # 순회하는 기준
            if a[j] > a[j+1] :
                a[j] , a[j+1] = a[j+1], a[j]
                cnt += 1
    print(f'Array is sorted in {cnt} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')

countSwaps([1,3,2,5,4])