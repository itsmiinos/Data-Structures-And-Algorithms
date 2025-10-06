# Last updated: 10/6/2025, 11:12:06 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        

        for i in range(len(asteroids)) : 
            destroyed = False
            while len(stack) > 0 and asteroids[i] < 0 < stack[-1] : 
                
                if abs(asteroids[i]) > stack[-1] : 
                    stack.pop(-1)
                
                elif abs(asteroids[i]) == stack[-1] :
                    stack.pop(-1)
                    destroyed = True
                    break
                
                elif abs(asteroids[i]) < stack[-1] : 
                    destroyed = True
                    break

            if destroyed == False : 
                stack.append(asteroids[i])
        
        return stack
            
                