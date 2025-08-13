# Last updated: 8/13/2025, 8:22:28 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = set(nums)
        
        max_count = 0
        for num in map : 
            count = 0
            if num-1 not in map : 
                current_number = num
                while current_number in map : 
                    count+=1
                    current_number +=1
            
                max_count = max(max_count , count)
        
        return max_count