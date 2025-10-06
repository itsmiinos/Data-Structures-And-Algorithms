# Last updated: 10/6/2025, 10:06:05 PM
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        k = ""

        for c in s : 

            if c == "]" :

                while len(stack) > 0 and stack[-1] != "[" :
                    curr = stack.pop(-1) + curr
                
                stack.pop(-1)

                while len(stack) > 0 and stack[-1].isdigit() : 
                    k = stack.pop(-1) + k
                
                stack.append(int(k) * curr)
                k = ""
                curr = ""
            
            else :

                stack.append(c)
        
        return "".join(stack)