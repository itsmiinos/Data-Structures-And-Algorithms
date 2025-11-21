# Last updated: 11/21/2025, 11:54:06 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value = set()
        for i in range(len(nums)) : 
            if nums[i] in value : 
                return True
            value.add(nums[i])
        
        return False