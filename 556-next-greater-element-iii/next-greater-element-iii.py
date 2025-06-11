class Solution:
    def nextGreaterElement(self, n: int) -> int:
        temp = n
        nums = []

        while temp>0 : 
            res = temp%10
            nums.append(res)
            temp = temp//10
        
        self.reverseArray(nums , 0 , len(nums)-1)
        dip_index = -1
        for i in range (len(nums)-1 , 0 , -1) : 
            if nums[i-1] < nums[i] :
                dip_index = i-1
                break

        if dip_index < 0 : 
            return -1
        
        next_greater_element = 0
        for i in range (len(nums)-1 , dip_index , -1) : 
            if nums[i] > nums[dip_index] : 
                next_greater_element = i
                break
        
        [nums[next_greater_element] , nums[dip_index]] = [nums[dip_index] , nums[next_greater_element]]

        self.reverseArray(nums , dip_index+1 , len(nums)-1)
        
        number = 0
        for i in range(len(nums)) : 
            number = (number * 10) + nums[i]

        if number >= 2**31 :
            return -1
        
        if number == n : 
            return -1
        
        return number

    def reverseArray(self , nums : [int] , left : int , right : int) : 
        while left<=right : 
            [nums[left] , nums[right]] = [nums[right] , nums[left]]
            left+=1
            right-=1
