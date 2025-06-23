class Solution:
    def nextGreaterElement(self, n: int) -> int:
        temp = n
        dip_index = 0
        
        nums = self.convertNumberToArrayAndReverse(n)

        n = len(nums)
        dip_index = -1
        for i in range(n-2 , -1 , -1) : 
            if nums[i] < nums[i+1] : 
                dip_index = i
                break

        if dip_index == -1 : 
            return -1
        
        next_greater_digit_index = 0
        for i in range(n-1 , dip_index , -1) : 
            if nums[i] > nums[dip_index] : 
                next_greater_digit_index = i
                break
        
        [nums[dip_index] , nums[next_greater_digit_index]] = [nums[next_greater_digit_index] , nums[dip_index]]

        self.reversePartOfArray(nums, dip_index+1 , n-1)
        n = self.convertArrayToNumber(nums)

        if n >= 2**31 :
            return -1
        
        return n
    
    def convertNumberToArrayAndReverse(self , n : int) -> [int] : 
        return [int(d) for d in str(n)]

    def reversePartOfArray(self , nums : [int] , start : int , end: int) : 
        while(start < end) : 
            [nums[start] , nums[end]] = [nums[end] , nums[start]]
            start+=1
            end-=1
    
    def convertArrayToNumber(self , nums : [int]) -> int : 
        number = 0

        for i in range(len(nums)) : 
            number = number*10 + nums[i]
        
        return number




