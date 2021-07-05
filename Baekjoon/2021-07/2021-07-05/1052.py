import sys
n, k = map(int,input().strip().split())

bucket = format(n,'b')
if bucket.count('1') <= k:
    print(0)
    sys.exit(0)
else :
    rq = ''
    l = 0
    for j in bucket :
        if j == '1':
            l += 1
            if l <= k:
                rq += j
            else :
                rq += '0'
        else :
            rq += '0'
val = '1'
for i in rq[::-1] :
    if i == '0' :
        val = val + '0'
    if i == '1' :
        break
print(int(val,2) - int(bucket[-len(val)+1:],2))

