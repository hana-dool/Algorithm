class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1 = ''.join(list(map(str,l1)))
        l2 = ''.join(list(map(str,l2)))
        l1 = l1[::-1]
        l2 = l2[::-1]
        i1 = int(l1)
        i2 = int(l2)
        i3 = i1+i2
        i3 = str(i3)
        i3 = i3[::-1]
        return list(map(int,list(i3)))

s = Solution()
print(s.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
