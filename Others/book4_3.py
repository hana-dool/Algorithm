x_a,y = list(str(input()))
y = int(y)
val = ['a','b','c','d','e','f','g','h']
num = [1,2,3,4,5,6,7,8]
dic = dict(zip(val,num))
x = dic[x_a]

dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

cnt = 0
for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8 :
        cnt += 1
print(cnt)

