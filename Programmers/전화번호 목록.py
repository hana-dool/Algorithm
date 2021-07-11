
lst_a = ["12","123","1235","567","88"]
lst_a_s = [i[::-1].zfill(20)[::-1] for i in lst_a ]
lst_n = list(zip(lst_a,lst_a_s))
lst_n.sort(key = lambda x : x[1])

def check(a,b):
    ch_a = a[0]
    ch_b = b[0]
    for i in range(len(ch_a)):
        if ch_a[i] != ch_b[i]:
            return True # 응 안겹쳐~
    else : # 엥 다통과?
        return False # 겹칩니다..

for i in range(len(lst_n)-1):
    if check(lst_n[i],lst_n[i+1]) :
        answer = True # 안겹침
    else :
        answer = False # 헉 겹침
        break

print(answer)

