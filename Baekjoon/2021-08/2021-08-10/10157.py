C,R = map(int,input().split())
K = int(input())
mat = [[0]*C for _ in range(R)]
# 시계 반대방향이 된다.
# 또한 출력시에도 x,y 가 -> y,x 가 되어야 한다.


start = [0,0]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
mat[0][0] = 1
def find_XY():
    i = -1
    x, y = 0, 0
    cnt = 1
    if K == 1 :
        print(1,1)
        return
    while True :
        i = (i+1)%4
        while 0<= x+dx[i] < R and 0 <= y+dy[i] < C and  mat[x+dx[i]][y+dy[i]] == 0 :
            nx = x+dx[i]
            ny = y+dy[i]
            mat[nx][ny] = mat[x][y] + 1
            if mat[nx][ny] == K :
                print(ny+1,nx+1)
                return
            cnt += 1
            x,y = nx,ny
        if cnt == C*R :
            break
    print(0)
    return
find_XY()