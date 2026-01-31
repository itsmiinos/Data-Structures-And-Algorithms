# Last updated: 1/31/2026, 8:44:14 PM
1class Solution:
2    def reverseByType(self, s: str) -> str:
3        result = ""
4        special_chars = []
5        special_index = set()
6        for i in range(len(s)-1 , -1 , -1) :
7            if s[i].isalpha() :
8                result += s[i]
9            else :
10                special_chars.append(s[i])
11                special_index.add(i)
12        
13        k = 0
14        for i in range(len(s)) :
15            if i in special_index :
16                result = result[:i] + special_chars[k] + result[i:]
17                k+=1
18
19            # print(result)
20        return result
21            
22        
23        