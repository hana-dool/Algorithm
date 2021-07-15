class Solution(object):
    def reverse(self, x):
        if x >= 0 :
            s = str(x)
            s = s[::-1]
            s = int(s)
        else  :
            s = str(x)
            s = s[1:]
            s = s[::-1]
            s = int(s)
            s = -1 * s 
        if not -1*2**31 <= s <= 2**31 -1 :
            return(0)
        else :
            return(s)
        """
        :type x: int
        :rtype: int
        """
# 무시무시하게 더럽네요.... ㅜㅜ