n = int(input().strip())


def ch_group(x):
    for i in set(x):
        cnt = x.count(i)
        idx = x.index(i)
        if len(set(x[idx:idx+cnt])) > 1 :
            return 0
    else :
        return 1
cnt = 0
for _ in range(n):
    cnt += ch_group(input().strip())
print(cnt)
