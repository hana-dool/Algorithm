import sys
input = sys.stdin.readline
S,P = map(int,input().split())
dna = input()
a,c,g,t = map(int,input().split())
cnt = 0

def check(dic) :
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t :
        return 1
    else :
        return 0

dic = {'A':dna[:P].count('A'),
       'C':dna[:P].count('C'),
       'G':dna[:P].count('G'),
       'T':dna[:P].count('T')}
cnt += check(dic)

for i in range(P,S) :
    if dna[i] in ('A','C','G','T') :
        dic[dna[i]] += 1
    if dna[i] in ('A','C','G','T') :
        dic[dna[i-P]] -= 1
    cnt += check(dic)
print(cnt)

