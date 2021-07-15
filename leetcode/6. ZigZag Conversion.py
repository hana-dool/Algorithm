class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 :
            return s
        order = [[] for _ in range(numRows)]
        lst = list(s)
        period = numRows * 2 - 2
        for i,v in enumerate(lst) :
            i_p = i % period
            if i_p <= (period // 2):
                order[i_p].append(v)
            else :
                order[period - i_p].append(v)
        strng = ''
        for i in order :
            strng = strng +''.join(i)
        return strng
