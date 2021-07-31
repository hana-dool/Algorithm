from itertools import permutations

def solution(expression):
    strng = ''
    lst_ = []
    for i in expression :
        if i.isdigit():
            strng+= i
        else :
            lst_.append(strng)
            lst_.append(i)
            strng = ''
    if strng :
        lst_.append(strng)
    operation = ['-','+','*']
    order = list(permutations(operation,3))
    ans_lst = []
    for operation_order in order :
        lst = lst_.copy()
        for i in operation_order :
            while len(lst) != 1 :
                for idx, element in enumerate(lst) :
                    if element == i :
                        new = eval(lst[idx-1] + lst[idx] + lst[idx+1])
                        lst[idx] = str(new)
                        lst.pop(idx-1)
                        lst.pop(idx)
                        break
                else :
                    break
        ans_lst.append(abs(int(lst[0])))
    answer = max(ans_lst)
    print(answer)
    return answer
solution("50*6-3*2")