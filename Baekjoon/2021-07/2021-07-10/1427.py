import sys
n = input()
lst = list(map(int,list(n)))
lst.sort(reverse = True)
print(''.join(map(str,lst)))