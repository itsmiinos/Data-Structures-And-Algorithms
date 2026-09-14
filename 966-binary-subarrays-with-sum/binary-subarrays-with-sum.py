class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.solve(nums , goal) - self.solve(nums , goal - 1)
    
    def solve(self , nums , goal) -> int :
        if goal < 0 :
            return 0

        i = 0
        j = 0
        count = 0
        bsum = 0

        while j < len(nums) :
            bsum += nums[j]

            while i < len(nums) and bsum > goal :
                bsum -= nums[i]
                i+=1

            count += (j - i + 1)
            
            j+=1
        
        return count