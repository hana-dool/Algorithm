class Solution(object):
    def longestCommonPrefix(self, strs):
        l = list(map(len, strs))
        l = min(l)
        k = ''
        tot = -1  # l 이 0 인 경우도 있기떄문에..
        for i in range(l):
            if all(strs[0][i] == j[i] for j in strs):
                tot = i
                continue
            else:
                tot = i - 1
                break
        return strs[0][:tot + 1]

        """
        :type strs: List[str]
        :rtype: str
        """