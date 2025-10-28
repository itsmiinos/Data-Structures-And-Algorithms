# Last updated: 10/29/2025, 12:18:59 AM
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)
        return self.solve(nums, target, dp)

    def solve(self, nums: List[int], target: int, dp: list[int]) -> int:
        # Base cases
        if target == 0:
            return 1
        if target < 0:
            return 0

        # Memoized result
        if dp[target] != -1:
            return dp[target]

        total = 0
        for num in nums:
            total += self.solve(nums, target - num, dp)

        dp[target] = total
        return dp[target]
