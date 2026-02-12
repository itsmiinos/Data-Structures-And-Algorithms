# Last updated: 2/12/2026, 11:35:34 AM
1class Solution:
2    def longestBalanced(self, s: str) -> int:
3        max_len = 0
4
5        for i in range(len(s)) :
6            lookup = collections.defaultdict(int)
7            for j in range(i , len(s)) :
8                lookup[s[j]] +=1
9                freq_check = lookup[s[j]]
10                flag = True
11                for key in lookup.keys() :
12                    if freq_check != lookup[key] :
13                        flag = False
14                
15                if flag == True :
16                    max_len = max(max_len , j - i + 1)
17        
18        return max_len