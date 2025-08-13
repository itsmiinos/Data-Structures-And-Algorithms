# Last updated: 8/13/2025, 8:22:56 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ansList = []
        result = self.helper(0 , nums , [] , ansList)
        return result
    
    def helper(self , index , nums , ds , ansList) : 
        ansList.append(ds[:])

        for i in range(index , len(nums)) : 
            if i > index and nums[i] == nums[i-1] : continue

            ds.append(nums[i])
            self.helper(i+1 , nums , ds , ansList)
            ds.pop(-1)
        
        return ansList
