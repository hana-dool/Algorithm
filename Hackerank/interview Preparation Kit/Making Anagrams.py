def cnt_alpha(x):
    dic = {}
    for i in x :
        dic[i] = dic.get(i,0) + 1
    return dic

def makeAnagram(a, b):
    dic_a = cnt_alpha(a)
    dic_b = cnt_alpha(b)
    inter = set(dic_a.keys()) | set(dic_b.keys())
    cnt = 0
    for i in inter :
        cnt += (abs(dic_a.get(i,0) -dic_b.get(i,0)))
    return(cnt)
