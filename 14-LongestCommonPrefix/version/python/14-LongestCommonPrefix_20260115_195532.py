# Last updated: 1/15/2026, 7:55:32 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        strs.sort()
4        i = -1
5        first_string = strs[0]
6        last_string = strs[-1]
7
8        while i < len(first_string) and i < len(last_string) : 
9            if i == len(first_string)-1 :
10                break
11            elif first_string[i+1] == last_string[i+1] :
12                i+=1
13            else :
14                break
15        
16        if i == -1 : 
17            return ""
18        else :
19            return first_string[:i+1]
20