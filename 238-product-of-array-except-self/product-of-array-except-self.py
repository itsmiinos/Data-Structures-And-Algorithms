class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        productArray = [-1]*n
        productArray[0] = nums[0]

        for i in range(1,n) :
            productArray[i] = productArray[i-1] * nums[i]
        
        multiplier = 1

        for i in range (n-1 , 0 , -1) :
            productArray[i] = multiplier * productArray[i-1]
            multiplier = multiplier * nums[i]
        productArray[0] = multiplier
        
        return productArray


    