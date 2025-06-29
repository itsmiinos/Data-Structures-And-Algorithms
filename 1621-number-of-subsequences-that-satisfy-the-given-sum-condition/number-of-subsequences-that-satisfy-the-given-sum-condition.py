class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        left = 0 
        right = len(nums)-1
        M = (10**9) + 7 
        total_subsequences = 0

        while left<=right : 
            if nums[left] + nums[right] > target : 
                right -=1
            
            if nums[left] + nums[right] <= target : 
                total_subsequences = int(total_subsequences%M) + int( 2**(right - left)%M)
                left+=1
        
        return total_subsequences
        
