import sys
read = sys.stdin.readline
T = int(read())
cnt = 0

val = [T] # 처음값!
j = 0

while True :
    new = []
    # 새로운 값들에 대해서! 가능한 모든 경우를 append 해 본다.
    for i in val:
        if i == 1 :
            j = 1
            break
        if i%3 == 0 :
            k = i//3
            new.append(k)
        if i%2 == 0 :
            k = i//2
            new.append(k)
        new.append(i-1)
    if j == 1 :
        break
    cnt += 1
    val = new.copy() # new 에 1값이 없었으므로 다시 갱신
print(cnt)