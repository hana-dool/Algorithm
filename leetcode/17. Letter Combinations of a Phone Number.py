class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        results = ['']
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        for nums in digits:
            s = []
            for d in map[nums]:
                for r in results:
                    s.append(r+d)
            results = s
        return results
