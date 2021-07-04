def minimumAbsoluteDifference(arr):
    arr.sort()
    ans = []
    for i in range(len(arr)-1):
        ans.append(abs(arr[i] - arr[i+1]))
    return(min(ans))

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = minimumAbsoluteDifference(arr)
print(result)