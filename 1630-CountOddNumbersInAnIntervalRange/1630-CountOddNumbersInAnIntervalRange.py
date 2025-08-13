# Last updated: 8/13/2025, 8:17:13 PM
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1)//2 - (low//2)