import sys
input = sys.stdin.readline

N , M = map(int,(input().split()))
st = set()
for _ in range(N) :
    st.add(input())
cnt = 0
for _ in range(M) :
    val = input()
    if val in st :
        cnt += 1
print(cnt)
