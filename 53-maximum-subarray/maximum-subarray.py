class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = -sys.maxsize

        for i in range (len(nums)) : 
            if sum < 0 :
                sum = nums[i]
            
            else : 
                sum = sum + nums[i]

            maxSum = max(maxSum , sum)
        return maxSum