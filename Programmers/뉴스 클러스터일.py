def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    lst1 = []
    lst2 = []
    for i in range(1,len(str1)):
        lst1.append(str1[i-1:i+1])
    for i in range(1,len(str2)):
        lst2.append(str2[i-1:i+1])
    lst_1 = []
    lst_2 = []
    for i in lst1:
        if i.isalpha():
            lst_1.append(i)
    for i in lst2:
        if i.isalpha():
            lst_2.append(i)
    intersect = set(lst_1) & set(lst_2)
    union = set(lst_1) | set(lst_2)
    cnt_inter = 0
    cnt_union = 0
    for i in intersect :
        cnt_inter += min(lst_1.count(i),lst_2.count(i))
    for i in union :
        cnt_union += max(lst_1.count(i),lst_2.count(i))
    if cnt_union == 0 :
        answer = 65536
    else :
        answer =int (( cnt_inter / cnt_union ) * 65536 )
    return answer

print(solution('aa1+aa2', 'AAAA12'))

