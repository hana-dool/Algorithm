n = int(input())
time = [tuple(map(int,input().strip().split())) for _ in range(n)]
time = sorted(time , key = lambda x : (x[1],x[0]))
cnt = 0
end = 0
for s,e in time :
    if end <= s :
        cnt += 1
        end = e
print(cnt)


#
# ## dp 실패!
# dp = [1] * n
# for i in range(n):
#     for j in range(i):
#         if time[i][0] >= time[j][1]:
#             dp[i] = max(dp[i],dp[j]+1)
# print(max(dp))