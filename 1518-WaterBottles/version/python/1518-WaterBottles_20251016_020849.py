# Last updated: 10/16/2025, 2:08:49 AM
class Solution:
    def numWaterBottles(self, b: int, n: int) -> int:
        return b + (b - 1) // (n - 1)