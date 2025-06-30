class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        maximum_index = 0
        longest_length = 0
        start = 0

        for i in range(len(nums)) : 
            while nums[i] - nums[start] > 1 : 
                start+=1
            
            if nums[i] - nums[start] == 1 : 
                longest_length = max(longest_length , i - start + 1)
               
        
        return longest_length

        # 1,3,2,2,5,2,3,7
        # 1 2 2 2 3 3 5 7 -> 1