# Last updated: 8/13/2025, 8:14:41 PM
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        count_even = sum(1 for num in nums if num%2==0)
        count_odd = n - count_even

        if abs(count_even - count_odd) > 1 : 
            return -1
        swaps = 0 
        if count_even > count_odd : 
            swaps = self.checkSwaps(True, nums)
        elif count_odd > count_even : 
            swaps = self.checkSwaps(False, nums)
        else :
            swaps = min(self.checkSwaps(True , nums) , self.checkSwaps(False , nums))
        return swaps

    def checkSwaps(self , starting_even : bool , nums : [int]) -> int : 
        n = len(nums)
        even = 0 if starting_even else 1
        swaps = 0
        for i in range(n) : 
            if nums[i]%2==0 : 
                swaps+= abs(i-even)
                even+=2

        return swaps
                