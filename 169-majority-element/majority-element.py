class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = 0
        count = 0

        for i in range(len(nums)) :
            if nums[i] == val :
                count+=1
            elif count == 0 :
                val = nums[i]
                count = 1
            else :
                count-=1
        
        return val