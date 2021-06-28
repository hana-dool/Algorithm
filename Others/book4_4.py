# N * M  크기의 직사각형
# 현재 위치에서 현재 방향을 기준으로 왼쪽방향으로부터 차례로 탐색한다.
# 캐릭터의 바로 왼쪽에 가보지 않은 칸이 존재하면 왼쪽방향으로 회전한 후 왼쪽으로 한칸 전진
# 왼쪽 방향에 가보지 않은 칸이 없다면 또 왼쪽으로 돌기

M,N = map(int,input().split())
x,y,d = map(int,input().split())
mat = [ list(map(int,input().split())) for _ in range(N)]


val = [0,1,2,3]
dir = [(-1,0),(0,1),(1,0),(0,-1)]
dic = dict(zip(val,dir))
cnt = 0


val_b = [0,1,2,3]
dir_b = [(0,-1),(-1,0),(0,1),(1,0)]
dic_b = dict(zip(val_b,dir_b))
k=0
rot = 0
mat[x][y] = 2
while True :
    # 각 방향에 대해서, direction 으로 이동할 곳을 update
    nx = x + dic[d][0]
    ny = y + dic[d][1]

    # update 한 곳에 대해서 조건에 맞는지 (이동할 수 있는지) 점검
    if 0 <= nx <= M-1 and 0 <= ny <= N-1 and mat[ny][nx] == 0 :
        # 이동할떄 위치 업데이트
        x,y = nx,ny

        # direction 또한 업데이트
        d = (d+3) % 4

        # 가본곳은 가본곳이라 업데이트 , 즉 2로 바꿈
        mat[ny][nx] = 2

        # cnt 1 셈
        cnt += 1

        # 몇번 돌았는지도 초기화
        rot = 0
        #
    else :
        d = (d + 3) % 4
        # 한번 돌기는 하였으므로 += 1
        rot += 1
    if rot == 4 :
        # 뒤로 가기
        x,y = x + dir_b[d][0] , y + dir_b[d][1]
        if mat[y][x] == 1 :
            break
        else :
            rot = 0
            cnt += 1
    print(mat)

# 언젠가는 if 를 만족하지 못하여 움직이지 못하게 된다.
print(cnt)





