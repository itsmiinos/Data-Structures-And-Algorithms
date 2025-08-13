# Last updated: 8/13/2025, 8:19:11 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        runningSum = [None]*len(nums)
        runningSum[0] = nums[0]

        for i in range(1, len(nums)) : 
            runningSum[i] = runningSum[i-1] + nums[i]

        for i in range(len(nums)) : 
            if i == 0 : 
                leftSum = 0 
                rightSum = runningSum[len(nums)-1] - runningSum[i]
            elif i == len(nums)-1 :
                leftSum = runningSum[i-1] 
                rightSum = 0
            else : 
                leftSum = runningSum[i-1]
                rightSum = runningSum[len(nums)-1] - runningSum[i]
            print(leftSum , rightSum)
            if leftSum == rightSum : 
                return i
        return -1
