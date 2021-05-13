N , K = map(int,input().split())
val = list(map(int,input()))

cnt = K
ch = 0
for i in range(10):
    stk = []
    if cnt == 0 : # cnt 0 이면 끝내자.
        break
    for j in val :
        if cnt == 0 : # 0 됫으면 뒤에꺼 다 가~
            stk.append(j)
            continue
        if i != j : # 값이 다르면
            stk.append(j) # 24363
        else :
            cnt -= 1
    val = stk # 업데이트
val = [str(_) for _ in val]
ans = ''.join(val)
print(ans)

stk = []
# 10 6
# 4032431950
a