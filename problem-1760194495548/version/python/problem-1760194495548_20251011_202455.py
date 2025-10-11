# Last updated: 10/11/2025, 8:24:55 PM
class Solution:
    def scoreBalance(self, s: str) -> bool:
        if not s : 
            return False
        
        # Convert each character to its alphabet score (a=1, b=2, ...)
        scores = [ord(c) - ord('a') + 1 for c in s]

        # Build prefix sum
        prefix = [0] * len(s)
        prefix[0] = scores[0]
        for i in range(1, len(s)):
            prefix[i] = prefix[i - 1] + scores[i]

        total = prefix[-1]

        # Try each split point
        for i in range(len(s) - 1):  # split between i and i+1
            left_sum = prefix[i]
            right_sum = total - prefix[i]
            if left_sum == right_sum:
                return True

        return False
            
            
            
            