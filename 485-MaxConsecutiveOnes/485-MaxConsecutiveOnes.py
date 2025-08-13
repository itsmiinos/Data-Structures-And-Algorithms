# Last updated: 8/13/2025, 8:19:38 PM
import math
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i in range (len(nums)) :
            if nums[i]==1 : 
                count+=1
            elif nums[i]==0 :
                count=0
            print(count)

            maxCount = max(count , maxCount)
        return maxCount