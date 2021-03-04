
import sys
read = sys.stdin.readline
N = int(read())
mat = [[0]*N for _ in range(N)] # N*N

for i in range(N) : # 0~N-1
    k = list(map(int,read().split()))
    for j in range(i+1): # 0~i
        mat[i][j] = k[j]


for k in range(N-1,-1,-1) : # N-1 ~ 0
    for j in range(k) :# 0 ~ k-1
        val = max(mat[k][j], mat[k][j+1])
        mat[k-1][j] += val
print(mat[0][0])

#-------------------- DFS 는 불가능 --------------------#
#
# max = 0
# # l 은 깊이
# # sum 은 합
# # j 는 이전의 index
# def DFS(l,sum,j) :
#     global max
#     if l == N-1 :
#         if sum > max :
#             max = sum
#     else :
#         DFS(l+1,sum+mat[l+1][j],j)
#         DFS(l+1,sum+mat[l+1][j+1],j+1)
#
# DFS(0,mat[0][0],0)
# print(max)
#------------------------------------------------------#
