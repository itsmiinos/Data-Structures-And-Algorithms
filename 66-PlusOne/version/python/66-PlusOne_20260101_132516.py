# Last updated: 1/1/2026, 1:25:16 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        sum = 0
4        i = len(digits)-1
5        carry = 1
6        result = []
7
8        while i >= 0 or carry != 0:
9            if i < 0 : 
10                sum = carry
11            else : 
12                sum = carry + digits[i]
13                
14            if sum <= 9 :
15                result.append(sum)
16                carry = 0
17            else :
18                carry = sum // 10
19                result.append(sum % 10)
20            
21            i-=1
22        result.reverse()
23        return result