from collections import deque

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        x = list(x)
        p = deque(x)
        while len(p) >= 2 :
            front = p.popleft()
            back = p.pop()
            if front != back :
                print('false')
                return
        print('true')
        return

x = 121
s = Solution()
s.isPalindrome(x)