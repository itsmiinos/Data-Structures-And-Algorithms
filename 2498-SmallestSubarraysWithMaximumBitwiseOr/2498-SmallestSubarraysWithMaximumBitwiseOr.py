# Last updated: 8/13/2025, 8:15:58 PM
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        setBits = [-1]*32
        result = []

        for i in range(len(nums)-1 , -1 , -1) : 
            
            endIndex = i

            for j in range(32) : 
                if (nums[i] & (1 << j)) : 
                    setBits[j] = i
                
                else :
                    if setBits[j] != -1 : 
                        endIndex = max(endIndex , setBits[j])
            
            result.append(endIndex - i + 1)
        result.reverse()
        return result