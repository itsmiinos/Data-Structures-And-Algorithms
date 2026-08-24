class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_numbers = set(nums)
        max_count = 0

        for num in all_numbers :
            if num+1 not in all_numbers :
                count = 0
                val = num
                while val in all_numbers :
                    count+=1
                    val-=1
                
                max_count = max(max_count , count)
        
        return max_count