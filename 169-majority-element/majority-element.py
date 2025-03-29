class Solution(object):
    def majorityElement(self, nums):
        count = 0
        number = nums[0]
        for item in nums :
            if item == number :
                count +=1
            elif count == 0 :
                number = item
                count = 1
            else :
                count -=1
        
        return number
        
        