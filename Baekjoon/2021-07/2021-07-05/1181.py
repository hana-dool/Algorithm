import functools
n = int(input())
lst = []
for _ in range(n):
    word = input()
    lst.append(word)

lst = list(set(lst))

def sort_strng(x,y):
    if len(x)>len(y): #x>y
        return 1
    elif x == y :
        return 0
    elif len(x) == len(y):
        ch_lst = [x,y]
        ch_lst.sort(reverse = True)
        if ch_lst[0] == x :
            return 1
        else :
            return -1
    else :
        return -1
lst.sort(key = functools.cmp_to_key(sort_strng))
for i in lst:
    print(i)


