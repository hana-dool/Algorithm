import sys
input = sys.stdin.readline
L,C = map(int,input().split())
lst = input().split()
moum = ('a','e','i','o','u')


from itertools import combinations
per = list(combinations(lst,L))
st = set()
for alpha in per :
    m_cnt = 0
    z_cnt = 0
    for i in alpha :
        if i in moum :
            m_cnt += 1
        else :
            z_cnt += 1
    if m_cnt >= 1 and z_cnt >= 2 :
        st.add(tuple(sorted(alpha)))
ans = list(st)
ans.sort()
for i in ans :
    print(''.join(i))

