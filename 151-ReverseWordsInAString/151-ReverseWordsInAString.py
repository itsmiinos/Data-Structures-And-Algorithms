# Last updated: 8/13/2025, 8:21:55 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])