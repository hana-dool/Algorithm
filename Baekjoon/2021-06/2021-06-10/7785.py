N = int(input())
dic = {}
for _ in range(N):
    s,b = input().split()
    if b == 'enter':
        dic[s] = True
    else :
        # 딕셔너리의 메모리를 줄여주기 위해서입니다.
        del dic[s]
for i in sorted(list(dic.keys()),reverse = True) :
    print(i)
