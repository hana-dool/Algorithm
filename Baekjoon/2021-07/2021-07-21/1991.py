import sys
input = sys.stdin.readline

n = int(input())
tree = dict()
for _ in range(n):
    node, left , right = input().split()
    tree[node] = [left,right]

def first(x):
    if x == '.' : # 아무것도 없는것에 다다르면 gg
        return
    else :
        print(x , end='')
        first(tree[x][0]) # 왼쪽부터 깊어지기~
        first(tree[x][1]) # 그 다음 깊어지기

def middle(x):
    if x == '.':
        return
    else :
        middle(tree[x][0]) # 있으면..
        print(x, end='')
        middle(tree[x][1]) # 있으면..

def last(x):
    if x =='.' :
        return
    else :
        last(tree[x][0])
        last(tree[x][1])
        print(x,end='')
first('A')
print('')
middle('A')
print('')
last('A')
