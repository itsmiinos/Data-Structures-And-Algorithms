class Solution:
    def rob(self, nums: List[int]) -> int:
        total_houses = len(nums)
        loot = [-1]*total_houses
        result = max(self.robHelper(total_houses-2 , nums , loot) , self.robHelper(total_houses-1 , nums , loot))
        return result

    def robHelper(self , n:int , nums:[int] , loot:[int]) -> int:
        if n == 0 or n == 1:
            return  nums[n]
        if n<0 or n>=len(nums):
            return 0
        if loot[n] !=-1 : return loot[n]
        a = self.robHelper(n-2 , nums, loot) + nums[n]
        b = self.robHelper(n-3 , nums , loot) + nums[n]
        loot[n] = max(a,b)
        return max(a,b)