N = int(input())
cnt = 0
if N <= 99:
    cnt = N
else:
    cnt += 99
    for i in range(100, N + 1):
        string = str(i)
        setting = set()
        for v in range(len(string) - 1):
            val = int(string[v]) - int(string[v + 1])
            setting.add(val)
        if len(setting) == 1:
            cnt += 1
print(cnt)