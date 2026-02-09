# Last updated: 2/9/2026, 9:12:10 PM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        stack = []
4
5        for i in range(len(asteroids)) :
6            destroyed = False
7            while stack and asteroids[i] < 0 and stack[-1] > 0 :
8                if stack[-1] < abs(asteroids[i]) :
9                    stack.pop(-1)
10                elif stack[-1] == abs(asteroids[i]) :
11                    stack.pop(-1)
12                    destroyed = True
13                    break
14                else :
15                    destroyed = True
16                    break
17            
18            if destroyed == False :
19                stack.append(asteroids[i])
20            
21        return stack
22            
23
24            
25