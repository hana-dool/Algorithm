def alternatingCharacters(s) :
    k = 0
    ans = []
    for i in range(len(s)-1) :
        if s[i] == s[i+1]:
            k += 1
        if s[i] != s[i+1] or i == len(s)-2 :
            ans.append(k)
            k = 0
    return(sum(ans))
