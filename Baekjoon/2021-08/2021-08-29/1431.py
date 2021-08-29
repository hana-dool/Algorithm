N = int(input())
lst = [input().strip() for _ in range(N)]
def order_function(x) :
    ans = []
    ans.append(len(x))
    cnt = 0
    for i in x :
        if i.isdigit() :
           cnt += int(i)
    ans.append(cnt)
    ans.append(x)
    return ans
for i in sorted(lst, key = order_function) :
    print(i)