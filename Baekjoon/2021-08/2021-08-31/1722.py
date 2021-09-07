import sys
input = sys.stdin.readline

def check_inside(x1,y1,x2,y2,X,Y) :
    if x1 < X < x2 and y1 < Y < y2 :
        return True
    else :
        return False
for _ in range(4) :
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
    x1,p1 = sorted([x1,p1])
    y1,q1 = sorted([y1,q1])
    x2,p2 = sorted([x2,p2])
    y2,q2 = sorted([y2,q2])
    edge1 = set()
    for i in range(x1,p1+1) :
        edge1.add((i,y1))
        edge1.add((i,q1))
    for j in range(y1,q1+1) :
        edge1.add((x1,j))
        edge1.add((p1,j))

    edge2 = set()
    for i in range(x2,p2+1) :
        edge2.add((i,y2))
        edge2.add((i,q2))
    for j in range(y2,q2+1) :
        edge2.add((x2,j))
        edge2.add((p2,j))
    cnt = 0
    union = []
    inside = 0
    for i in edge2 :
        if check_inside(x1,y1,p1,q1,i[0],i[1]) :
            inside += 1
    for i in edge1 :
        if check_inside(x2,y2,p2,q2,i[0],i[1]) :
            inside += 1
    for i in edge2 :
        if i in edge1 :
            union.append(i)
            cnt += 1
    if cnt == 4 :
        Xs = list(map(lambda x: x[0], union))
        Ys = list(map(lambda x: x[1], union))
        if len(set(Xs)) == 1 or len(set(Ys)) == 1 :
            print('b')
        else :
            print('a')
    elif inside != 0 :
        print('a')
    elif cnt > 1 :
        print('b')
    elif cnt == 1 :
        print('c')
    elif cnt == 0 :
        print('d')



