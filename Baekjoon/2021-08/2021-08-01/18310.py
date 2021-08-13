import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
lst.sort()
l = len(lst)
place = l//2 + l%2 - 1
antena = lst[place]
print(antena)
# [1,3,4,5,6] -> 2
# [1,5,7,9] -> 2


dic = {}
dic[2] = 1
dic[3] = 3
dic[1] = 5
dic

= dict(zip(keys,vals))
