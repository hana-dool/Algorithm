
# array 에서 찾는 것은 target 이며 그 범위는 start ~ end 임
def binary(array,target,start,end) :
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return(mid)
        elif array[mid] > target :
            end = mid -1
        elif array[mid] < target :
            start = mid + 1
    return(-1) # 만약 찾는게 없을때에

array = [1,4,6,8,13,23,43]
target = 13
start = 1
end = 6
k = binary(array, target, start, end)
print(k)