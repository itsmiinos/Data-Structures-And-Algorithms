# Last updated: 2/3/2026, 8:22:27 PM
1from collections import defaultdict
2class Solution:
3    def numberOfSubstrings(self, s: str) -> int:
4        right = 0
5        left = 0
6        result = 0
7        lookup = defaultdict(int)
8
9        while right < len(s) :
10            lookup[s[right]] +=1
11
12            while len(lookup) == 3 :
13                result += len(s) - right
14                lookup[s[left]] -=1
15                if lookup[s[left]] == 0 :
16                    del lookup[s[left]]
17                
18                left+=1
19        
20            right +=1
21        
22        return result