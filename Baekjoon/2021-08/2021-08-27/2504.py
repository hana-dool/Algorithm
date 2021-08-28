import sys
from collections import deque
input = sys.stdin.readline
lst = deque(list(input().strip()))
stack = []
def convert_num(lst) :
    temp = []
    for i in lst :
        if not temp :
            temp.append(i)
        else :
            if str(i).isdigit() :
                if str(temp[-1]).isdigit() :
                    val = temp.pop()
                    temp.append(int(val)+int(i))
                else :
                    temp.append(i)
            elif i == ')' :
                if temp[-1] == '(' :
                    temp.pop()
                    temp.append(2)
                elif str(temp[-1]).isdigit() :
                    if len(temp) == 1 :
                        return False
                    if temp[-2] == '(' :
                        val = temp.pop()
                        temp.pop()
                        temp.append(int(val)*2)
                    elif temp[-2] == '[' :
                        return False
                    else :
                        temp.append(i)
                else :
                    temp.append(i)
            elif i == ']' :
                if temp[-1] == '[' :
                    temp.pop()
                    temp.append(3)
                elif str(temp[-1]).isdigit() :
                    if len(temp) == 1 :
                        return False
                    if temp[-2] == '[' :
                        val = temp.pop()
                        temp.pop()
                        temp.append(int(val)*3)
                    elif temp[-2] == '(' :
                        return False
                    else :
                        temp.append(i)
                else :
                    temp.append(i)
            else :
                temp.append(i)
    return temp
# convert {] to number !
while True :
    temp = lst.copy()
    lst = convert_num(lst)
    if not lst :
        print(0)
        sys.exit(0)
    if len(temp) == len(lst):
        break
if len(lst) > 1 :
    print(0)
else :
    if str(lst[0]).isdigit() :
        print(lst[0])
    else :
        print(0)
