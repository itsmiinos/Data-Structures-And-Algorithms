# Last updated: 10/2/2025, 4:07:53 PM
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        

        for c in s : 
            if c != "]" :
                stack.append(c)
            else : 
                curr = ""
                while stack[-1] != "[" : 
                    curr =  stack.pop(-1) + curr
                
                stack.pop()
                k = ""
                while len(stack) > 0 and stack[-1].isdigit() : 
                    k = stack.pop() + k

                stack.append(int(k) * curr) 
        
        return "".join(stack)