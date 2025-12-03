# Last updated: 12/3/2025, 11:01:57 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        left = 0
4        right = 0
5        maxFreq = 0
6        maxLength = 0
7        freq = [0] * 26
8
9        while right < len(s) :
10            freq[ord(s[right]) - ord('A')] +=1
11            maxFreq = max(freq)
12
13            while (right - left + 1) - maxFreq > k :
14                val = s[left]
15                freq[ord(val) - ord('A')] -=1
16                left +=1
17
18            if (right - left + 1) - maxFreq <= k : 
19                maxLength = max(maxLength , right - left + 1)
20
21            right +=1
22
23        return maxLength