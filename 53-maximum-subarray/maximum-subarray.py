class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        maxSum = -sys.maxint
        for item in nums :
            if sum < 0 :
                sum = item
            else : 
                sum = sum + item
            maxSum = max(sum , maxSum)
        
        return maxSum
        