# Last updated: 2/9/2026, 8:11:02 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pair = [(p,s) for p,s in zip(position, speed)]
4        pair.sort(reverse = True)
5        stack = []
6
7        for p,s in pair:
8
9            #calculate the time needed to reach the target
10            time = (target-p)/s
11
12            if stack and stack[-1]>=time:
13                continue
14
15            #only push when time higher than top of stack(slower cars)
16            stack.append(time)
17        return len(stack)
18