class Solution:
    def threeSum(self, nums):
        answer = set()
        nums.sort()
        l = len(nums)
        st = set(nums)
        for start in range(l):
            for end in range(start+1,l):
                if -nums[start]-nums[end] in st :
                    # 겹치는 경우...
                    if -nums[start]-nums[end] == nums[start] :
                        if nums[start+1] == nums[start] :
                            add = (nums[start],nums[start],nums[end])
                            add = tuple(sorted(add))
                            answer.add(add)
                    elif -nums[start]-nums[end] == nums[end] :
                        if nums[end-1] == nums[end] :
                            add = (nums[start],nums[end],nums[end])
                            add = tuple(sorted(add))
                            answer.add(add)
                    else :
                        add = (nums[start], -nums[start]-nums[end], nums[end])
                        add = tuple(sorted(add))
                        answer.add(add)
        return(list(map(list,answer)))
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))

r=(1,3,5,-2)
sorted(r)