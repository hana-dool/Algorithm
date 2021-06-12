# 선택 정렬
# 정렬되어있지 않은 데이터중 가장 작은 데이터를 선택해, 맨 앞부터 순서대로 정렬한다.
# 3241
# 1324
# 1234
# .... 옆과 같이 제일 작은값을 찾아서 제일 앞으로 보낸다.


# input = [1,3,2,4] 와 같은 list 형태
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j] :
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]
    return arr



def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
print(bubble_sort([1,5,2,4,3]))
