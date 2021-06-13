import sys
read = sys.stdin.readline


while True :
    w,h = map(int,read().split())
    if (w,h) == (0,0):
        break
    mat = [list(map(int,read().split())) + [0] for _ in range(h)]
    mat.append([0]*(w+1))

cnt = 0
def DFS(x):
    

