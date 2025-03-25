class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)) :
            diff = target - nums[i] 
            for j in range(len(nums)):
                if nums[j] == diff and i!= j :
                    return [i,j]