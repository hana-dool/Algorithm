class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def dfs(depth,S,left,right) :
            if depth == 2*n :
                if S.count('(') == S.count(')') :
                    ans.append(S)
                return
            if left > n :
                return
            if left > right :
                dfs(depth+1,S + '(',left+1,right )
                dfs(depth+1,S + ')',left  ,right+1)
            else :
                dfs(depth+1,S + '(',left+1,right)
        dfs(0,'',0,0)
        return ans
