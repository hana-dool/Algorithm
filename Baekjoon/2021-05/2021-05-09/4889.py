import sys
read = sys.stdin.readline
idx = 0
while True :
    idx += 1
    l = list(read().strip())
    if l[0] == '-' :
        break
    stk = []
    cnt = 0
    # 즉 { 를 만나면 그냥 넣고, } 를 만나면 뺴버리기
    for i in l :
        if i == '{':
            stk.append('{')
        else : # } 를 만났다?
            if stk : # 비어있지 않으면
                stk.pop()
            else : # 비어있다면
                stk.append('{')
                cnt += 1 # 한차례 더해주어야 한다.
    if stk : # 비어있지 않다면 {{{{{ 형식일것.
        cnt += len(stk) // 2
    print(f'{idx}. {cnt}')



# {{}}{}
# {}} -> }
# {{{{{{