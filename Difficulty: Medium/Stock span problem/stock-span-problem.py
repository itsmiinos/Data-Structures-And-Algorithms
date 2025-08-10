class Solution:
    def calculateSpan(self, arr):
        # code here
        stack = []
        result = [1]*len(arr)
        
        for i in range(len(arr)) : 
            span_value = 1
            while len(stack) > 0 and stack[-1][0] <= arr[i] : 
                popped = stack.pop(-1)
                index = popped[1]
                span_value += result[index]
            
            stack.append([arr[i] , i])
            result[i] = span_value
        
        return result