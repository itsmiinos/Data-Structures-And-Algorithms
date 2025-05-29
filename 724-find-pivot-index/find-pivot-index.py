class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [-1]*len(nums)

        prefixSum[0] = nums[0]

        for i in range(1 , len(nums)) :
            prefixSum[i] = prefixSum[i-1] + nums[i]
        
        for i in range(0 , len(nums)) :
            leftSum = prefixSum[i - 1] if i > 0 else 0
            rightSum = prefixSum[len(nums)-1] - prefixSum[i]
            if leftSum == rightSum : 
                return i

        return -1