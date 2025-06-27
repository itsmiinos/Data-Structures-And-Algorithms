class Solution:
    def calculateSpan(self, arr):
        #write code here
        stack = []
        ans = [0]*len(arr)
        
        for i in range(len(arr)) : 
            while len(stack) > 0 and arr[i] >= stack[-1].val :
                stack.pop(-1)
            
            if not stack : 
                ans[i] = i+1
            
            else : 
                ans[i] = i - stack[-1].index
            
            stack.append(Pair(arr[i], i))
        return ans
            
        

class Pair :
    
    def __init__ (self , value : int , index : int) :
        self.val = value
        self.index = index
