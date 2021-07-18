# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         mx = max(height)
#         l = len(height)
#         h = list(zip(height,list(range(l))))
#         dic = dict()
#         for x in h :
#             dic[x[0]] = dic.get(x[0],[]) + [x[1]]
#         ans = []
#         for i in range(1,mx+1): # 높이
#             temp = []
#             for j in range(i,mx+1):
#                 temp.extend(dic.get(j,[])) # 가로길이 다 넣기
#             if temp :
#                 ans.append(i * (max(temp) - min(temp)))
#         return(max(ans))
#
# s = Solution()
# s.maxArea([1,1])
#
#위 풀이는 시간초과.. 다른 풀이 요망

class Solution(object):
    def maxArea(self, height):
        l = len(height)
        start = 0
        end = l-1
        mx = 0
        while start != end :
            w = end - start
            h = min(height[end],height[start])
            if mx < w*h :
                mx = w*h
            if height[end] > height[start] :
                start += 1
            else :
                end -= 1
        return(mx)

s = Solution()
s.maxArea( [1,8,6,2,5,4,8,3,7])
