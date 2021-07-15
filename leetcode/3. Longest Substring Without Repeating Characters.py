from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        stack = deque([])
        lst = deque(list(s))
        st = set()
        mx = 0
        while True :
            if not lst :
                break
            v = lst.popleft()
            if v in stack :
                while True :
                    if not stack :
                        stack= deque([v])
                        break
                    if stack[0] != v :
                        stack.popleft()
                    else :
                        stack.popleft()
                        stack.append(v)
                        break
            else :
                stack.append(v)
                if mx < len(stack) :
                    mx = len(stack)
        print(mx)
S = Solution()
S.lengthOfLongestSubstring("aab")



## 다시
from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        stack = deque([])
        lst = deque(list(s))
        mx = 0
        while True :
            if not lst :
                break
            v = lst.popleft()
            if v in stack :
                while v in stack :
                    stack.popleft()
                stack.append(v)
            else :
                stack.append(v)
                if mx < len(stack):
                    mx = len(stack)
        print(mx)
S = Solution()
S.lengthOfLongestSubstring("aab")