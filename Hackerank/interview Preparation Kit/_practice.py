def quick_sort(array):
    # 리스트가 하나 이하의 원소를 담고있으면 정료
    if len(array) <= 1 :
        return array
    pivot = array[0] # 피벗은 첫번쨰 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [ x for x in tail if x <= pivot ]
    right_side = [x for x in tail if x > pivot ]

    # 분할 이후, 왼쪽 부분과 오른쪽 부분에서 각걱 정렬을 수행한 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def count_sort(array):
    # 0 ~ 의 값이 있다고 가정.
    count = [0] * (max(array) + 1)
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i,end = ' ')

count_sort([3,2,64,3,5,2,3,1,2,2])