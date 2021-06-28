n,m,k = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort(reverse = True)
x,y = lst[0],lst[1]

# k 번 반복할 수 있음 ..
p = m//(k+1)
print(y * p + x * (m-p))

