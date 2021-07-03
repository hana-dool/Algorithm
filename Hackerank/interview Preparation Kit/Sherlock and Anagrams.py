import math
def comb(x,y):
    '''
    :param x: xCy 계산
    :param y:
    :return:가짓수(int)
    '''
    if y > x :
        return(0)
    val = math.factorial(x) / (math.factorial(y) * math.factorial(x-y) )
    return int(val)

def sherlockAndAnagrams(s):
    total = 0
    dic = {}
    for i in range(0, len(s)): # 시작점
        for j in range(1,len(s)-i+1): # 끝점
            strng = ''.join(sorted(s[i:i+j]))
            dic[strng] = dic.get(strng,0)  + 1
    for val in dic.values():
        total += comb(val,2)
    return total

sherlockAndAnagrams('ifailuhkqq')


sorted('adeb')