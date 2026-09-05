class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefixMax = [None]*len(nums)
        suffixMin = [None]*len(nums)

        prefixMax[0] = nums[0]
        for i in range(1 , len(nums)) :
            prefixMax[i] = max(prefixMax[i-1] , nums[i])
        
        suffixMin[-1] = nums[-1]
        for i in range(len(nums)-2 , -1 , -1) :
            suffixMin[i] = min(suffixMin[i+1] , nums[i])
        
        for i in range(len(nums)) :
            if prefixMax[i] - suffixMin[i] <= k :
                return i
        
        return -1