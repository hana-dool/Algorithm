lst = ['c=','c-','d-','lj','nj','s=']
lst2 = ['dz=','z=']

strng = input()

num = 0
ans = 0
for i in lst :
    num += (strng.count(i) * 2)
    ans += strng.count(i)

num += (strng.count('dz=') * 3)
ans += strng.count('z=')
num += (strng.count('z=')  - strng.count('dz=') ) * 2
print(len(strng)-num + ans)
