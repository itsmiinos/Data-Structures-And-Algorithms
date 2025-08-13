# Last updated: 8/13/2025, 8:16:17 PM
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum_of_subarray_minnimums = self.sumOfSubarrayMinnimums(nums)
        sum_of_subarray_maximums = self.sumOfSubarrayMaximums(nums)

        return sum_of_subarray_maximums - sum_of_subarray_minnimums
    
    def sumOfSubarrayMinnimums(self , nums : list[int]) -> int : 
        last_smaller_element = [-1]*len(nums)
        next_smaller_element = [len(nums)]*len(nums)

        left_stack = []
        for i in range(len(nums)-1 , -1 , -1) : 

            while len(left_stack) > 0 and left_stack[-1][0] > nums[i] : 
                popped = left_stack.pop(-1)
                popped_index = popped[1]

                last_smaller_element[popped_index] = i
            
            left_stack.append([nums[i] , i])
        
        right_stack = []
        for i in range(len(nums)) : 

            while len(right_stack) > 0 and right_stack[-1][0] >= nums[i] : 
                popped = right_stack.pop(-1)
                popped_index = popped[1]

                next_smaller_element[popped_index] = i
            
            right_stack.append([nums[i] ,i])

        sum = 0
        for i in range(len(nums)) : 
            left_range = i - last_smaller_element[i] 
            right_range = next_smaller_element[i] - i

            sum += nums[i] * (right_range * left_range)

        return sum 

    def sumOfSubarrayMaximums(self , nums : list[int]) -> int : 
        last_larger_element = [-1]*len(nums)
        next_larger_element = [len(nums)]*len(nums)

        left_stack = []
        for i in range(len(nums)-1 , -1 , -1) : 

            while len(left_stack) > 0 and left_stack[-1][0] < nums[i] : 
                popped = left_stack.pop(-1)
                popped_index = popped[1]

                last_larger_element[popped_index] = i
            
            left_stack.append([nums[i] , i])
        
        right_stack = []
        for i in range(len(nums)) : 

            while len(right_stack) > 0 and right_stack[-1][0] <= nums[i] : 
                popped = right_stack.pop(-1)
                popped_index = popped[1]

                next_larger_element[popped_index] = i
            
            right_stack.append([nums[i] ,i])

        sum = 0
        for i in range(len(nums)) : 
            left_range = i - last_larger_element[i] 
            right_range = next_larger_element[i] - i

            sum += nums[i] * (right_range * left_range)

        return sum 
