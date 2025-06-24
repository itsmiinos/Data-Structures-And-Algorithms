class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)

        prefixMax = [None]*n
        suffixMin = [None]*n

        prefixMax[0] = arr[0]
        for i in range(1 , n) : 
            prefixMax[i] = max(prefixMax[i-1] , arr[i])
        
        suffixMin[n-1] = arr[n-1]
        for i in range(n-2 , -1 , -1) : 
            suffixMin[i] = min(suffixMin[i+1] , arr[i])

        count = 0 

        for i in range(n-1) : 
            if prefixMax[i] <= suffixMin[i+1] : 
                count+=1
        
        return count+1