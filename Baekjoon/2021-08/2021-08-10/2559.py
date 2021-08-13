N,K = map(int,input().split())
lst = list(map(int,input().split()))
l = len(lst)
ans = []
val = 0
start = 0
s = sum(lst[:K])
ans.append(s)
while start <= l-K-1:
    s = s - lst[start] + lst[K+start]
    ans.append(s)
    start += 1
print(max(ans))