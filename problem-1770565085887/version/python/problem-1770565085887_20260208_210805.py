# Last updated: 2/8/2026, 9:08:05 PM
1class Solution:
2    def mergeAdjacent(self, nums: List[int]) -> List[int]:
3        stack = []
4        i = 0
5
6        while i < len(nums) :
7            val = nums[i]
8            while len(stack) > 0 and stack[-1] == val :
9                popped = stack.pop(-1)
10                val = val + popped
11
12            stack.append(val)
13            i+=1
14
15        return stack