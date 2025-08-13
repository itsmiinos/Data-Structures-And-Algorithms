# Last updated: 8/13/2025, 8:18:11 PM
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        m = len(popped)
        stack = []
        if n!= m : 
            return False
        i = 0
        j = 0
        while i < n and j < m: 
            if len(stack) == 0 : 
                stack.append(pushed[i])
                i+=1
            
            else : 
                if popped[j] != stack[-1] : 
                    if i < n : 
                        stack.append(pushed[i])
                        i+=1
                    else : 
                        return False
                
                elif popped[j] == stack[-1] : 
                    stack.pop(-1)
                    j+=1
        
        if j < n : 
            while len(stack) > 0 and popped[j] == stack[-1] : 
                stack.pop(-1)
                j+=1
            if j < n and popped[j] != stack[-1] :
                return False
        
        return True