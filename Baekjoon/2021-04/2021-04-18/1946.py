# 1946
import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T) :
    N = int(read())
    lis = []
    cnt = 0
    for _ in range(N):
        val = list(map(int,read().split()))
        lis.append(val)
    lis.sort(key = lambda x : x[0]) # sort
    min = lis[0][1]
    for i in range(N):
        if lis[i][1] < min :
            min = lis[i][1]
            cnt += 1
    print(cnt+1)







# [(3, 2), (1, 4), (4, 1), (2, 3), (5, 5)]
# [ (1,4) (2,3) (3,2) (4,1) (5,5) ]



# [ 1  4

# min = 4 / (2  4), ///. .?
# [(1, 4), (2, 5), (3, 6), (4, 2),  (5, 7), (6, 1) , (7, 3),]
# 즉 다 떨어지는 사람은 뽑지 않는다는것이이네

# 둘다 떨어지는 실력을 가지고있는데요..?
