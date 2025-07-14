class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1]*len(nums)
        stack = []

        i = 0 
        while i < 2 * len(nums) : 
            curr = nums[i%len(nums)]
            while len(stack) > 0 and nums[stack[-1]] < curr : 
                index = stack.pop(-1)
                result[index] = curr
            if i < len(nums) : 
                stack.append(i)
            i+=1

        return result
