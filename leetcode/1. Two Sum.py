def twoSum(nums, target):
    dic = dict()
    ans = []
    for i, v in enumerate(nums):
        if target - v in dic:
            ans.extend([dic[target - v], i])
            break
        else:
            dic[v] = i
    print(ans)

twoSum([3,2,4],6)
