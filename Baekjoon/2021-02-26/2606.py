# https://www.acmicpc.net/problem/2606

# N : 컴퓨터의 수
# M : 연결되어있는 컴퓨터 쌍의 수
import sys
read = sys.stdin.readline

N = int(read())
M = int(read())
lis = [[] for _ in range(N+1)]

# 연결 정보를 생성하기 위한 리스트
for _ in range(M):
    start , end =map(int,read().split())
    lis[start].append(end)
    lis[end].append(start)
# 그러면 [[],[2,3],[4,2,5] ... ] 의 연결정보가 뜬다.

position = [0]*(N+1)
def DFS(l,cur) :
    global position
    for i in lis[cur] : # i 는 갈 수 있는 위치
        if position[i] == 0  : # 중복되서 가기 싫다는 뜻
           position[i] = 1 # 1로 갔었음을 표시
           DFS(l+1,i)

DFS(0,1)
print(sum(position)-1)



