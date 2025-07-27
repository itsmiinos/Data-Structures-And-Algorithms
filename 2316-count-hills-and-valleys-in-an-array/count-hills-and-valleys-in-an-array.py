class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        prev = nums[0]

        for i in range(1 , len(nums)-1) : 
            if nums[i] == nums[i+1] : 
                continue
            
            if (nums[i] < prev and nums[i] < nums[i+1] ) or (nums[i] > prev  and nums[i] > nums[i+1]) : 
                count+=1
            
            prev = nums[i]
        
        return count