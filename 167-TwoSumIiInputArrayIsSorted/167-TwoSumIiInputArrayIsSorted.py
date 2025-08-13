# Last updated: 8/13/2025, 8:21:36 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pointer1 = 0
        pointer2 = len(nums)-1

        while pointer1 < pointer2 : 

            if nums[pointer1] + nums[pointer2] == target : 
                return [pointer1+1 , pointer2+1] 

            elif nums[pointer1] + nums[pointer2] < target : 
                pointer1 +=1
            
            else : 
                pointer2 -=1
        
        return [pointer1+1 , pointer2+1]