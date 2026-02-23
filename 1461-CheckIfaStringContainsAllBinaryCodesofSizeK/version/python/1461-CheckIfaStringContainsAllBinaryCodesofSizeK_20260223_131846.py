# Last updated: 2/23/2026, 1:18:46 PM
1class Solution:
2    def hasAllCodes(self, s: str, k: int) -> bool:
3        left = 0
4        right = k-1
5        ans = [False]*(2**k)
6
7        while right < len(s) :
8            num = self.convertBinaryToDecimal(s , left , right)
9            if num < (2 ** k) :
10                ans[num] = True
11
12            right+=1
13            left+=1
14        
15        for i in range(len(ans)) :
16            if ans[i] == False :
17                return False
18        
19        return True
20    
21    def convertBinaryToDecimal(self , s : str , left : int , right : int) -> int :
22        num = 0
23        power = 0
24        for i in range(right , left-1 , -1) :
25            num += (2 ** power) * int(s[i])
26            power+=1
27    
28        return num