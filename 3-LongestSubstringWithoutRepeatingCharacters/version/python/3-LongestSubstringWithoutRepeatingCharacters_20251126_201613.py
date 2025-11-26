# Last updated: 11/26/2025, 8:16:13 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        chars = set()
4        left = 0
5        right = 0
6        max_length = 0
7
8        while right < len(s) : 
9            if s[right] not in chars : 
10                chars.add(s[right])
11                max_length = max(max_length , right - left + 1)
12                right+=1
13            else : 
14                while s[right] in chars : 
15                    l = s[left]
16                    chars.remove(l)
17                    left+=1
18        
19        return max_length