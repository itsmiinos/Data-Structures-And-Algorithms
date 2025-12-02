# Last updated: 12/2/2025, 9:57:44 PM
1from collections import defaultdict
2class Solution:
3    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
4        group = {}
5
6        for i in range(len(strs)) :
7            count = self.checkCount(strs[i])
8            if count in group : 
9                group[count].append(strs[i])
10            else :
11                group[count] = []
12                group[count].append(strs[i])
13        
14        result = []
15        for value in group.values() :
16            result.append(value)
17        
18        return result
19    
20
21    def checkCount(self , word : int) :
22        count = [0] * 26
23        for ch in word:
24            count[ord(ch) - ord('a')] += 1
25
26        return tuple(count)