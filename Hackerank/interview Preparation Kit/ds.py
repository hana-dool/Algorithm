arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

def hourglassSum(arr):
    dx = [-1,-1,-1,0,1,1,1]
    dy = [-1,0,1,0,-1,0,1]
    ans = []
    for x in range(6):
        for y in range(6):
            val = 0
            for d in range(7):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < 6 and 0 <= ny < 6 :
                    val += arr[nx][ny]
                    continue
                else :
                    break
            else :
                ans.append(val)
    print(max(ans))

result = hourglassSum(arr)


