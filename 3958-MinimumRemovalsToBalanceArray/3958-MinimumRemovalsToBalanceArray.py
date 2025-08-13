# Last updated: 8/13/2025, 8:14:44 PM
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_length = float('-inf')

        for right in range(len(nums)) : 
            while nums[right] > nums[left] * k : 
                left +=1

            max_length = max(max_length , right - left + 1)

        return len(nums) - max_length