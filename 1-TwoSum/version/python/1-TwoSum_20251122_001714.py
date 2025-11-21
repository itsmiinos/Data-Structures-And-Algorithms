# Last updated: 11/22/2025, 12:17:14 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)) : 
            d = target - nums[i]
            if d in diff : 
                return [diff[d] , i]
            diff[nums[i]] = i
     