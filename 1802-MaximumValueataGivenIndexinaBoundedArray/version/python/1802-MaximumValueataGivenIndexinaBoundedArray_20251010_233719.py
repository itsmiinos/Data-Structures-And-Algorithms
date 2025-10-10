# Last updated: 10/10/2025, 11:37:19 PM
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # Binary search for the highest possible value at index
        low, high = 1, maxSum
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            # Calculate total sum if nums[index] = mid
            total = self.sum_side(mid - 1, index) + self.sum_side(mid - 1, n - index - 1) + mid

            if total <= maxSum:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

    def sum_side(self, peak_minus_one: int, length: int) -> int:
        """
        Calculates the sum on one side of the peak.
        If peak_minus_one = 4 and length = 3, we get 4 + 3 + 2 = 9.
        If length is longer than peak_minus_one, the remaining are 1's.
        """
        if length <= peak_minus_one:
            # strictly decreasing slope down to peak - length
            last = peak_minus_one - length + 1
            return (peak_minus_one + last) * length // 2
        else:
            # fill up to 1s after hitting 1
            decreasing_sum = (peak_minus_one * (peak_minus_one + 1)) // 2
            ones = length - peak_minus_one
            return decreasing_sum + ones
