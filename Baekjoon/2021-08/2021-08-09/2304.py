import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    place, height = map(int,input().split())
    lst.append((place,height))
lst_raw = sorted(lst,key= lambda x : x[0])
mx = max(lst_raw)
# 제일 같거나 큰 부분 증가수열
# max 값을 만난 이후부터난 같거나 작은 감소수열
ans = []
start = 0
lst = lst_raw.copy()
while lst :
    h = lst.pop(0)
    if start <= h[1] :
        ans.append(h)
        start = h[1]
lst = lst_raw.copy()
lst = lst[::-1]
start = 0
ans2 = []
mx = max(lst,key=lambda x : x[1])[1]
while lst :
    h = lst.pop(0)
    if h[1] == mx :
        ans2.append(h)
        break
    if start <= h[1] :
        ans2.append(h)
        start = h[1]
cnt = 0
for i in range(len(ans)-1):
    cnt += (ans[i+1][0]-ans[i][0])*ans[i][1]
for i in range(len(ans2)-1):
    cnt += (ans2[i][0]-ans2[i+1][0])*ans2[i][1]
cnt += mx
print(cnt)

