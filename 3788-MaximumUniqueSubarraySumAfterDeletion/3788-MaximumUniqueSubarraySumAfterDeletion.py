# Last updated: 8/13/2025, 8:14:53 PM
from collections import OrderedDict

class Solution:
    def maxSum(self, nums: List[int]) -> int:

        # Remove duplicates while keeping order
        my_set = set()
        mn = float('-inf')
        sum = 0

        for i in range(len(nums)) : 
            if nums[i] not in my_set : 
                if nums[i] >= 0 : 
                    sum+=nums[i]
                else : 
                    mn = max(mn , nums[i])
            
            my_set.add(nums[i])
            
        if sum == 0 and 0 not in my_set : 
            return mn
            
        
        return sum