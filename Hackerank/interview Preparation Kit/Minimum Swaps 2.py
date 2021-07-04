# 아니 이게 왜됨?

def minimumSwaps(arr):
    cnt = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            k = arr[i]
            if k != i+1 :
                arr[i],arr[k-1] = arr[k-1], arr[i]
                cnt += 1
    return(cnt)

minimumSwaps([1,3,5,2,4,6,7])


