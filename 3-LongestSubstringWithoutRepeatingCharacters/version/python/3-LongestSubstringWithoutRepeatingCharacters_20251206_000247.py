# Last updated: 12/6/2025, 12:02:47 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        chars = set()
4        left = 0
5        right = 0
6        maxLength = 0
7
8        while right < len(s) : 
9            
10            while s[right] in chars : 
11                val = s[left]
12                chars.remove(val)
13                left+=1
14            
15            chars.add(s[right])
16            maxLength = max(maxLength , right - left + 1)
17
18            right +=1
19        
20        return maxLength
21