# Last updated: 8/13/2025, 8:23:08 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i) :
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
        