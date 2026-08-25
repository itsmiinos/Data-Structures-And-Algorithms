class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        my_set = set(nums)
        i = 1
        while k*i in my_set :
            i+=1
        
        return k*i