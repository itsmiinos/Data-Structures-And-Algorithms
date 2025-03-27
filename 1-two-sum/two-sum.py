class Solution(object):
    def twoSum(self, nums, target):
        sumMap = {}
        diff = 0
        for i in range(len(nums)) :
            diff = target - nums[i]
            if diff in sumMap :
                return [i,sumMap[diff]]
            else :
                sumMap[nums[i]] = i
        return -1