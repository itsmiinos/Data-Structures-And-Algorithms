# Last updated: 8/13/2025, 8:19:53 PM
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)) : 
            while stack and k > 0 and int(num[i]) < int(stack[-1]) : 
                stack.pop(-1)
                k-=1
            
            stack.append(num[i])
        
        while k > 0 :
            stack.pop(-1)
            k-=1
        
        
        first_index = 0
        for i in range(len(stack)) : 
            if stack[i] != "0" : 
                first_index = i
                break
        # print(first_index , stack)
        result = ''.join(stack[first_index: ]).lstrip("0")
        
        return result if result else "0"