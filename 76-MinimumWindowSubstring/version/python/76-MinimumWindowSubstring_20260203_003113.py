# Last updated: 2/3/2026, 12:31:13 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        freq = collections.defaultdict(int)
4
5        for c in t :
6            freq[c] +=1
7        
8        left = 0
9        right = 0
10        start = -1
11        min_len = float('inf')
12        count = 0
13
14        while right < len(s) :
15            if freq[s[right]] > 0 :
16                count+=1
17
18            freq[s[right]] -=1
19            
20            while count == len(t) :
21                if right - left + 1 < min_len :
22                    min_len = right - left + 1
23                    start = left
24                
25                freq[s[left]] +=1
26
27                if freq[s[left]] > 0 :
28                    count-=1
29                
30                left+=1
31            
32            right+=1
33        
34        if start == -1 :
35            return ""
36        
37        return s[start : start + min_len]