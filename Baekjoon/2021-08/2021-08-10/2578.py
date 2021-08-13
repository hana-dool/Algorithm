mat = []
for _ in range(5) :
    mat.append(list(map(int,input().split())))

ch = []
for _ in range(5):
    ch.append([0]*5)

ans = []
for _ in range(5):
    ans.extend(list(map(int,input().split())))

def find_idx(val) :
    for x in range(5) :
        for y in range(5) :
            if mat[x][y] == val :
                return (x,y)

def check_bingo(ch) :
    num = 0
    for x in range(5) :
        row_bingo = 0
        for y in range(5):
            row_bingo += ch[x][y]
        if row_bingo == 5 :
            num += 1

    for y in range(5) :
        col_bingo = 0
        for x in range(5) :
            col_bingo += ch[x][y]
        if col_bingo == 5 :
            num += 1

    dig_bingo = 0
    for y in range(5) :
        dig_bingo += ch[y][y]
    if dig_bingo == 5 :
        num +=1

    dig_bingo = 0
    for x in range(5) :
        dig_bingo += ch[4-x][x]
    if dig_bingo == 5 :
        num += 1
    return num


def find_minimum():
    for i in range(25):
        now_x, now_y = find_idx(ans[i])
        ch[now_x][now_y] = 1
        if check_bingo(ch) >= 3 :
            print(i+1)
            return

find_minimum()
