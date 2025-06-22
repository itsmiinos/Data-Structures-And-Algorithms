class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        runningMax = [None]*n
        backwardMax = [None]*n

        runningMax[0] = height[0]
        for i in range(1 , n) : 
            runningMax[i] = max(runningMax[i-1] , height[i])
        
        backwardMax[n-1] = height[n-1]
        for i in range(n-2 , -1 , -1):
            backwardMax[i] = max(backwardMax[i+1] , height[i])
        
        total_collection = 0
        for i in range(n) : 
            total_collection += min(runningMax[i] , backwardMax[i]) - height[i]
        
        return total_collection