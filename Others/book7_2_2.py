N = int(input())
lst1 = list(map(int,input().split()))
M = int(input())
lst2 = list(map(int,input().split()))


array = [0] * 1000000
for i in lst1 :
    array[i] = 1
for j in lst2 :
    if array[j] == 1 :
        print('yes' , end = ' ')
    else :
        print('no', end = ' ')