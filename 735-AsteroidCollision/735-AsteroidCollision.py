# Last updated: 8/13/2025, 8:19:10 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids : 
            while stack and stack[-1] > 0 and a < 0 and stack[-1] < abs(a):
                stack.pop()

            if not stack or stack[-1] < 0 or a > 0:
                stack.append(a)
            elif stack[-1] == -a:
                stack.pop()  # same size, both destroyed

        
        return stack