class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        stack = []
        stack.append(nums[0])
        stack.append(nums[1])
        count = 0
        for i in range(1,len(nums)) : 
            if len(stack) > 1 and stack[-1] != nums[i] : 
                last = nums[i]
                middle = stack[-1]
                first = stack[-2]
                print(first , middle , last)
                if (last < middle and middle > first) or (last > middle and middle < first) : 
                    count+=1
                stack.append(nums[i])
        
        return count