# Last updated: 8/19/2025, 9:13:30 PM
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total =0
        count =0
        for n in nums:
            if n ==0:
                count=count+1
            else:
                total += count * (count + 1) // 2
                count=0
        total += count * (count + 1) // 2
        return total