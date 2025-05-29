class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = [-1]*len(nums)

        prefixSum[0] = nums[0]

        for i in range(1 , len(nums)) :
            prefix = prefixSum[i-1]+nums[i]
            prefixSum[i] = prefix
        
        return prefixSum