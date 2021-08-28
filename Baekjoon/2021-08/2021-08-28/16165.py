import sys
input = sys.stdin.readline
from collections import defaultdict

N , M = map(int,input().split())

dic_team = defaultdict(list)
dic_mem = defaultdict(str)
for _ in range(N) :
    team_name = input().strip()
    member_num = int(input())
    for _ in range(member_num) :
        member = input().strip()
        dic_team[team_name].append(member)
        dic_mem[member] = team_name
for _ in range(M) :
    problem = input().strip()
    type = int(input())
    if type == 1 :
        print(dic_mem[problem])
    else :
        ans_lst = dic_team[problem]
        for i in sorted(ans_lst) :
            print(i)
