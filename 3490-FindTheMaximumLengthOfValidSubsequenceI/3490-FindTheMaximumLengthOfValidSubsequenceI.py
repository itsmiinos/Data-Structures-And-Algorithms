# Last updated: 8/13/2025, 8:15:11 PM
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        countEven = 0
        countOdd = 0

        for i in range(len(nums)) : 
            if nums[i] % 2 == 0 : 
                countEven+=1
            else :
                countOdd+=1
        
        alternatingCount = 1
        parity = nums[0] % 2

        for i in range(len(nums)) : 
            currParity = nums[i] % 2
            if currParity != parity : 
                alternatingCount+=1
                parity = currParity
        
        return max(countEven , countOdd , alternatingCount)