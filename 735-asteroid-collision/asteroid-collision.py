class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for curr in asteroids : 
            survives = True
            while len(stack) > 0 and curr < 0 and stack[-1] > 0 : 
                if stack[-1] < -curr : 
                    stack.pop()
                    continue
                
                elif stack[-1] == -curr : 
                    stack.pop()
                    survives = False
                    break
                
                else : 
                    survives = False
                    break
            
            if survives == True : 
                stack.append(curr)
    
        return stack
