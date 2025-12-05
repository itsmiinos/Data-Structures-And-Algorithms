# Last updated: 12/5/2025, 9:35:51 PM
1from collections import defaultdict
2class Solution:
3    def minWindow(self, s: str, t: str) -> str:
4        #step 1 -> measure the freq of the target
5
6        hashmap = defaultdict(int)
7        for i in range(len(t)) :
8            hashmap[t[i]] +=1
9        
10        #step 2 -> do sliding window for getting the min string
11        left = 0
12        right = 0
13        minLength = float('inf')
14        sIndex = -1
15        eIndex = -1
16        count = 0
17
18        while right < len(s) :
19            if hashmap[s[right]] > 0 :
20                count +=1
21            
22            hashmap[s[right]] -=1
23
24            while count == len(t) :
25
26                if right - left + 1 < minLength : 
27                    minLength = right - left + 1
28                    sIndex = left
29                    eIndex = right
30
31                hashmap[s[left]] +=1
32
33                if hashmap[s[left]] > 0 : 
34                    count-=1
35                
36                left +=1
37            
38            right+=1
39        
40        if sIndex == -1 : 
41            return ""
42        
43        return s[sIndex : sIndex + minLength]
44        
45            