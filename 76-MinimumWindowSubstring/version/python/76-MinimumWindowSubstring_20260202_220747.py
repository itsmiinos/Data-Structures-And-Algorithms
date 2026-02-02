# Last updated: 2/2/2026, 10:07:47 PM
1from collections import defaultdict
2class Solution:
3    def minWindow(self, s: str, t: str) -> str:
4        freq = defaultdict(int)
5
6        for i in range(len(t)) :
7            freq[t[i]] +=1
8        
9        count = len(t)
10        required = count
11
12        left = 0
13        right = 0
14        min_len = float('inf')
15        start = -1
16
17        while right < len(s) :
18
19            if freq[s[right]] > 0 :
20                count-=1
21            
22            freq[s[right]]-=1
23
24            while count == 0 :
25                if right - left + 1 < min_len :
26                    min_len = right - left + 1
27                    start = left
28
29                freq[s[left]] +=1
30
31                if freq[s[left]] > 0 :
32                    count +=1
33                
34                left+=1
35            
36            right+=1
37        
38        return "" if start == -1 else s[start:start + min_len]
39        
40