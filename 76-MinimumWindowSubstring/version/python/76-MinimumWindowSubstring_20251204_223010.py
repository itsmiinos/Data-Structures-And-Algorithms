# Last updated: 12/4/2025, 10:30:10 PM
1from collections import defaultdict
2
3class Solution:
4    def minWindow(self, s: str, t: str) -> str:
5        hashmap = defaultdict(int)
6        for i in range(len(t)) : 
7            hashmap[t[i]] +=1
8        
9        left = 0
10        right = 0
11        sIndex = -1
12        minLength = float('inf')
13        count = 0
14
15        while right < len(s) :
16            if hashmap[s[right]] > 0 : 
17                count +=1
18            hashmap[s[right]] -=1
19
20            while count == len(t) :
21                if minLength > right - left + 1 : 
22                    minLength = right - left + 1
23                    sIndex = left
24                
25                hashmap[s[left]] +=1
26                
27                if hashmap[s[left]] > 0 : 
28                    count -=1
29                
30                left +=1
31
32            right +=1
33        
34        if sIndex == -1 : 
35            return ""
36        
37        return s[sIndex : sIndex + minLength]