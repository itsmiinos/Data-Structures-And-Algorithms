class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack = []
        ans = [-1]*len(arr)
        
        for i in range(len(arr)) : 
            if len(stack) > 0 and arr[i] > stack[-1] .val : 
                while len(stack) > 0 and arr[i] > stack[-1].val :
                    popped = stack.pop(-1)
                    ans[popped.index] = arr[i] 
            stack.append(Pair(arr[i] , i))
        
        while len(stack) > 0 :
            popped = stack.pop(-1)
            ans[popped.index] = -1 
        
        return ans

class Pair : 
    
    def __init__(self, value : int , index : int) :
        self.val = value
        self.index = index