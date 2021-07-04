

n,r,c = map(int,input().strip().split())

def binary(x,n):
    ans = []
    while True :
        i = x % 2
        x = x // 2
        ans.insert(0,i)
        if x == 0 :
            break
    strng = ''.join(map(str,ans))
    rst= strng.zfill(2*n)
    return(rst)

b_r = binary(r,n)
c_r = binary(c,n)

dic = {'00' : 0 , '01':1, '10':2, '11':3}

gg = 0
for i in range(1,len(b_r)+1) :
    ch = b_r[-i] + c_r[-i]
    gg += ( dic[ch] * (4**(i-1)) )
print(gg)

