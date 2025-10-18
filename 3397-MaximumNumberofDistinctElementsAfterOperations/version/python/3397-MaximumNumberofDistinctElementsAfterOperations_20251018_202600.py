# Last updated: 10/18/2025, 8:26:00 PM
class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        count = 0
        last_used = -10**18  # very small number

        for num in nums:
            # Try to place current number as early as possible
            new_val = max(num - k, last_used + 1)
            if new_val <= num + k:
                count += 1
                last_used = new_val  # reserve this value

        return count
