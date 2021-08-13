
n = int(input())
lst = list(map(int,input().split()))
x = int(input())
st = set(lst)
cnt = 0

for i in lst :
    if i == x/2 :
        continue
    elif x-i in st :
        cnt += 1
        st.remove(i)
        st.remove(x-i)
print(cnt)