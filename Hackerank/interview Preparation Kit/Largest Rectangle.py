
def max_rec(h,i):
    val = 0
    lst = []
    for j in h :
        if j >= i :
           val += 1
        else :
            lst.append(val)
            val = 0
    lst.append(val)
    return(max(lst))

def largestRectangle(h):
    mx = max(h)
    ans = []
    for i in range(1,mx+1):
        ans.append(i * max_rec(h,i))
    return(max(ans))


print(largestRectangle([1,2,3,4,5]))
