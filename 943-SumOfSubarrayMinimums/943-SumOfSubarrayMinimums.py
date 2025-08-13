# Last updated: 8/13/2025, 8:18:21 PM
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left_smaller_element = [-1]*len(arr)
        right_smaller_element = [len(arr)]*len(arr)
        mod = (10**9) + 7

        left_stack = []
        for i in range(len(arr)-1 , -1 , -1) : 
            while len(left_stack) > 0 and arr[i] < left_stack[-1][0] : 
                popped = left_stack.pop(-1)
                popped_value = popped[0]
                popped_index = popped[1]

                left_smaller_element[popped_index] = i
            
            left_stack.append([arr[i] , i])
        
        right_stack = []
        for i in range(len(arr)) : 
            while len(right_stack) > 0 and arr[i] <= right_stack[-1][0] : 
                popped = right_stack.pop(-1)
                popped_value = popped[0]
                popped_index = popped[1]

                right_smaller_element[popped_index] = i
            
            right_stack.append([arr[i] , i])

        total = 0
        for i in range(len(arr)):
            left_count = i - left_smaller_element[i]
            right_count = right_smaller_element[i] - i
            total += arr[i] * left_count * right_count
            total %= mod

        return total