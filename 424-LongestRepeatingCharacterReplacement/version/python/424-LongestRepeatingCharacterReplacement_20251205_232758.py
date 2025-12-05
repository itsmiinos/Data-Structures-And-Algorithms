# Last updated: 12/5/2025, 11:27:58 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        freq = [0]*26
4        left = 0
5        right = 0
6        maxLength = 0
7
8        while right < len(s) : 
9            freq[ord(s[right]) - ord('A')] +=1
10
11            while (right - left + 1) - max(freq) > k : 
12                freq[ord(s[left]) - ord('A')] -=1
13                left+=1
14            
15            maxLength = max(maxLength , right - left + 1)
16            right +=1
17        
18        return maxLength