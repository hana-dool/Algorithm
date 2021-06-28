N = int(input())
lst1 = list(map(int,input().split()))
M = int(input())
lst2 = list(map(int,input().split()))

lst1.sort() # 찾고자 하는 lst

def binary(array,target,start,end):
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return(mid)
        elif array[mid] < target :
            start = mid + 1
        else :
            end = mid - 1
    return(None) # 없을떄..

for i in lst2 :
    if binary(lst1,i,0,len(lst1)) :
        print('yes', end= ' ')
    else :
        print('no', end = ' ')


