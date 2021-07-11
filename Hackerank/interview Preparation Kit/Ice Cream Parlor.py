# 아래는 겁나 많은 시간으로 폐기된 식/
def whatFlavors(cost, money):
    l = len(cost)
    order = list(range(l))
    lst = list(zip(cost,order))
    lst.sort(key = lambda x : x[0])
    for i in range(l): # l-1 까지
        for j in range(i+1,l): # i ~ l-1 까지
            if lst[i][0] + lst[j][0] == money :
                ans = [lst[i][1]+1,lst[j][1]+1]
                ans.sort()
                print(*ans)
                break
            elif lst[i][0] + lst[j][0] > money :
                break

def whatFlavors(cost, money):
    dic = {}
    for idx,val in enumerate(cost):
        if money - val in dic :
            print(f'{dic[money-val]+1} {idx+1}')
        else :
            dic[val] = idx

whatFlavors([4,3,2,5,7],5)


# 1 4 5 3 2
# 1 2 3 4 5

# 1 2 3 4 5
# 1 5 4 2 3 ( 변하게 된다. )
