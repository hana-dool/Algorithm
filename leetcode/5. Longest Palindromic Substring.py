class Solution(object):
    def longestPalindrome(self, s):
        l = len(s)
        mx = 0
        for i in range(l):
            for j in range(i+1,l+1):
                strng = s[i:j]
                if strng == strng[::-1]:
                    if mx < len(strng):
                        mx = len(strng)
                        rst = strng
        return(rst)

S = Solution()
print(S.longestPalindrome('ac'))


# 다른 풀이

class Solution(object):
    def longestPalindrome(self, s):
        l = len(s)
        mx = 0
        for j in range(l,0,-1): # j 는 길이가 된다.
            for i in range(l):
                if i+j <= l :
                    strng = s[i:i+j]
                    if strng == strng[::-1]:
                        print(strng)
                        rst = strng
                        return(rst)
S = Solution()
print(S.longestPalindrome("cbbd"))

for i in range(10,0,-1):
    print(i)