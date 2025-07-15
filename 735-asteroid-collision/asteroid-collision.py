class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)) : 
            survives = True

            while len(stack) > 0 and asteroids[i] < 0 and stack[-1] > 0 : 
                
                if -asteroids[i] > stack[-1] : 
                    stack.pop()
                    continue
                
                elif stack[-1] > -asteroids[i] : 
                    survives = False
                    break
                
                elif stack[-1] == -asteroids[i] : 
                    stack.pop()
                    survives = False
                    break
            
            if survives : 
                stack.append(asteroids[i])

        return stack