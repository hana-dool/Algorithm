while True :
    strng = input().rstrip()
    if strng == '.' :
        break
    stack = []
    for i in strng:
        if i == '(':
            stack.append(i)
        elif i == '[' :
            stack.append(i)
        elif i == ')':
            if (not stack) or stack[-1] !='(':
                print('no')
                break
            else :
                stack.pop()
        elif i == ']' :
            if (not stack) or stack[-1] !='[':
                print('no')
                break
            else :
                stack.pop()
    else :
        if stack : # 스택이 안비어있음
            print('no')
        else : # 스택이 비어있음
            print('yes')
