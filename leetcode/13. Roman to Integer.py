class Solution(object):
    def romanToInt(self, s):
        transform_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        transform_2 = {'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200}
        tot = 0
        strng = s
        for key, nums in transform_1.items():
            tot += strng.count(key) * nums
        for key, nums in transform_2.items():
            tot += strng.count(key) * nums
        return tot
        """
        :type s: str
        :rtype: int
        """
