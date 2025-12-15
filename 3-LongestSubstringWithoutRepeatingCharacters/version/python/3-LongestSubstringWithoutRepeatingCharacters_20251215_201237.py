# Last updated: 12/15/2025, 8:12:37 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        chars = set()
4        left = 0
5        right = 0
6        max_length = 0
7
8        while right < len(s) :
9
10            while s[right] in chars : 
11                chars.remove(s[left])
12                left+=1
13            
14            chars.add(s[right])
15
16            max_length = max(max_length , right - left + 1)
17            right +=1
18        
19        return max_length
20        
21