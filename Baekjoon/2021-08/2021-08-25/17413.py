import sys
from collections import deque
input = sys.stdin.readline
strng = input().rstrip()

def find_tag(lst):
    l = len(lst)
    for i in range(l):
        if lst[i] == '>' :
            end = i
            break
    ans1 = lst[:end+1]
    ans2 = lst[end+1:]
    return ans1, ans2

def find_alpha(lst) :
    l = len(lst)
    end = l
    for i in range(l) :
        if not ( lst[i].isalpha() or lst[i].isdigit() ) :
            end = i
            break
    ans1 = lst[:end]
    ans2 = lst[end:]
    return ans1[::-1] , ans2

def cut_words(word):
    lst = list(word)
    ans = []
    while len(lst) > 0 :
        if lst[0] == '<' :
            temp , lst = find_tag(lst)
            ans.append(temp)
        elif lst[0].isalpha() or lst[0].isdigit():
            temp, lst = find_alpha(lst)
            ans.append(temp)
        elif lst[0] ==' ' :
            lst.pop(0)
            ans.append(' ')
    return ans

def paste(strng) :
    return(''.join(strng))

print(''.join(list(map(paste,cut_words(strng)))))


