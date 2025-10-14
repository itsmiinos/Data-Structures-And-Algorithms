# Last updated: 10/14/2025, 9:32:57 PM
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        pre, curr = 0, 1
        
        for i in range(1, len(nums)): 
            if nums[i] > nums[i - 1]: curr += 1 
            else: 
                pre = curr 
                curr = 1 
            
            if curr >= k and pre >= k or curr // 2 >= k: return True
        return False 
        