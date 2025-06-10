class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        value = nums[0]
        n = len(nums)

        for i in range(1 , n) : 
            if nums[i] == value : 
                count +=1
            if nums[i] != value : 
                count -=1
            if count == 0 : 
                value = nums[i]
                count = 1
        
        return value