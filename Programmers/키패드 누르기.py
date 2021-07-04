
key = [1,2,3,4,5,6,7,8,9,'*',0,'#']
lst2 = [1,0,1,2,1,2,3,2,3,4,3,4]
lst5 = [2,1,2,1,0,1,2,1,2,3,2,3]
lst8 = [3,2,3,2,1,2,1,0,1,2,1,2]
lst0 = [4,3,4,3,2,3,2,1,2,1,0,1]

dic2 = dict(zip(key,lst2))
dic5 = dict(zip(key,lst5))
dic8 = dict(zip(key,lst8))
dic0 = dict(zip(key,lst0))

lstck = ['*']
rstck = ['#']
ans = []

def ch(i,dic2,lstck,rstck,hand,ans):
    if dic2[lstck[-1]] > dic2[rstck[-1]]:
        rstck.append(i)
        ans.append("R")
    elif dic2[lstck[-1]] < dic2[rstck[-1]]:
        lstck.append(i)
        ans.append('L')
    else:
        if hand == 'right':
            rstck.append(i)
            ans.append('R')
        else:
            lstck.append(i)
            ans.append('L')
    return(ans)

def solution(numbers, hand):
    ans = []
    for i in numbers:
        if i in (1,4,7):
            lstck.append(i)
            ans.append('L')
        elif i in (3,6,9):
            rstck.append(i)
            ans.append('R')
        else :
            if i == 2 :
                ch(i, dic2, lstck, rstck, hand, ans)
            elif i == 5 :
                ch(i, dic5, lstck, rstck, hand, ans)
            elif i == 8 :
                ch(i, dic8, lstck, rstck, hand, ans )
            else :
                ch(i, dic0, lstck, rstck, hand, ans)
    return(''.join(ans))

print(solution( [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'right'))
