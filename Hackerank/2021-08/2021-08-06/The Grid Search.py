def check(x,y) :
    # r is row
    # c is col
    for i in range(r) :
        for j in range(c) :
            if G[x+i][y+j] != P[i][j] :
                return False
    return True

def gridSearch(G, P):
    for i in range(R) :
        for j in range(C) :
            if i+r<=R and j+c<= C :
                if check(i,j) :
                    return 'YES'
    return 'NO'
    # Write your code here

# 실버 3~4 난이도인듯