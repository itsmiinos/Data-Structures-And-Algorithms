class Solution:
    def leftSmaller(self, arr):
        
        stack = []
        result = [None]*len(arr)
        
        for i in range(len(arr)-1 , -1 , -1) : 
            while len(stack) > 0 and stack[-1][0] > arr[i] :
                popped = stack.pop(-1)
                value = popped[0]
                index = popped[1]
                result[index] = arr[i]
            
            stack.append([arr[i] , i])
        
        while len(stack) > 0 : 
            popped = stack.pop(-1)
            index = popped[1]
            result[index] = -1
        
        return result