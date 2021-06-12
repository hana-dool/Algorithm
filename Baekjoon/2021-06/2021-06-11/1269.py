k = input()
A = set(input().split())
B = set(input().split())
C1 = A - B
C2 = B - A
s = C1 | C2

print(len(s))