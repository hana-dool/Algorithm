
def hr(steps, path):
    p = list(path)
    lv = 0
    cnt = 0
    lst = []
    for i in p :
        if i == 'U':
            lv += 1
        else :
            lv -= 1
        lst.append(lv)
    for i in range(1,len(lst)) :
        if lst[i-1] < 0 and lst[i] >= 0 :
            cnt += 1
    return(cnt)
hr(8,'UDDDUDUU')
