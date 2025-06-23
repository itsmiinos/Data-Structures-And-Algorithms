class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = nums[0]
        count = 1
        
        n = len(nums)
        for i in range(1 , len(nums)) : 
            if nums[i] == val : 
                count+=1
            elif count == 0 and nums[i]!=val: 
                val = nums[i]
                count+=1
            else : 
                count-=1
        
        return val