# Last updated: 8/13/2025, 8:16:09 PM
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []

        for i in range(len(nums)) : 
            if nums[i] == key : 
                starting_point = max(0 , i-k)
                ending_point = min(len(nums)-1 , i+k)
                for j in range (starting_point , ending_point+1) : 
                    if abs(i-j)<=k : 
                        if len(result)==0 : 
                            result.append(j)
                        elif j > result[len(result)-1] : 
                            result.append(j)
        
        return result