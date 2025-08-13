# Last updated: 8/13/2025, 8:17:54 PM
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in range(len(s)) : 
            char = s[i]
            if len(stack) > 0 and char == stack[-1] : 
                stack.pop(-1)
                continue
            stack.append(char)
        
        result = ""
        for i in range(len(stack)) : 
            result += stack[i]
        
        return result
        
