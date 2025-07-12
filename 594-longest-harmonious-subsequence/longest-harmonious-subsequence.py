class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        longest_length = 0
        start = 0

        for i in range(len(nums)) : 

            while nums[i] - nums[start] > 1 : 
                start+=1
            
            if nums[i] - nums[start] == 1 :
                longest_length = max(longest_length , i - start + 1)
        
        return longest_length