# Last updated: 11/23/2025, 8:21:31 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                # remove until duplicate removed
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1

        return max_length