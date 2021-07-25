import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def getPostorder(nums):
    length = len(nums)
    if length <= 1:
        return nums
    for i in range(1, length):
        if nums[i] > nums[0]:
            return getPostorder(nums[1:i]) + getPostorder(nums[i:]) + [nums[0]]
    return getPostorder(nums[1:]) + [nums[0]]

nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

nums = getPostorder(nums)
for n in nums:
    print(n)














import sys
sys.setrecursionlimit(10**6)

lst = []
while True :
    try :
        lst.append(int(input()))
    except :
        break

def change(x):
    l = len(x)
    key = x[0]
    for i in range(1,l) :
        if key < x[i]:
            break
    x[1:i] + x[i:] + x[0]
    change(x[1:i])
    change(x[i:])
        # 모든 순서를 키 / 왼 / 오 -> 왼 -> 오 -> 키















