class Solution(object):
    def singleNumber(self, nums):
        uniqueElement = 0
        for item in nums :
            uniqueElement ^=item
        
        return uniqueElement
        