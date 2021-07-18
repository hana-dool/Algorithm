def solution(absolutes, signs):
    l = len(absolutes)
    ans = 0
    for i in range(l):
        if signs[i] :
            ans += absolutes[i]
        else :
            ans -= absolutes[i]
    answer = ans
    return answer


