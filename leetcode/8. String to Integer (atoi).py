class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        val = 1
        if s :
            if s[0] == '-':
                val = -1
                s = s[1:]
            elif s[0] == '+':
                val = 1
                s = s[1:]
            else :
                val = 1
        strng = ''
        exit = 0
        k = len(s)
        for i in range(k) :
            if s[i].isdigit():
                strng = strng + s[i]
            else :
                break
        if not strng :
            return 0
        ans = val*int(strng)
        if ans < -2**31 :
            ans = -2**31
        elif ans > 2**31 - 1 :
            ans = 2**31 - 1
        return ans
s = Solution()
print(s.myAtoi("4193 with words"))



from collections import deque
deque([1,2,3],)