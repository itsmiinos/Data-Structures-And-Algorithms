class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        

        next_greater_stack = []
        n = len(nums)
        new_array = nums
        for i in range(len(nums)) : 
            new_array.append(nums[i])
        
        next_greater = [-1]*len(new_array)

        i = 0
        while i < len(new_array) : 

            while len(next_greater_stack) > 0 and next_greater_stack[-1][0] < new_array[i] : 
                popped = next_greater_stack.pop(-1)
                popped_element = popped[0]
                popped_index = popped[1]

                next_greater[popped_index] = new_array[i]
            
            next_greater_stack.append([new_array[i] , i])
            i+=1
        
        result = []
        for i in range(n) : 
            result.append(next_greater[i])
        
        return result
        