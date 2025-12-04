# Last updated: 12/4/2025, 9:32:42 PM
1from collections import defaultdict
2class Solution:
3    def minWindow(self, s: str, t: str) -> str:
4        left = 0
5        right = 0
6        hashmap = defaultdict(int)
7        min_length = float('inf')
8        sIndex = -1
9
10        for i in range(len(t)) : 
11            hashmap[t[i]] +=1
12        needed = len(t)
13        cnt = 0
14        while right < len(s) :
15            if hashmap[s[right]] > 0 :
16                cnt +=1
17            hashmap[s[right]]-=1
18            
19            while cnt == needed : 
20                if right - left + 1 < min_length : 
21                    min_length = right - left + 1
22                    sIndex = left
23                
24                hashmap[s[left]] +=1
25                if hashmap[s[left]] > 0 : 
26                    cnt -=1
27                
28                left +=1
29            
30            right +=1
31        
32        if sIndex == -1 : 
33            return ""
34        
35        return s[sIndex : sIndex + min_length]