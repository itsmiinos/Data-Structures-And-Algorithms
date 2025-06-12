class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0 
        prefixMax = [0]*len(arr)
        suffixMin = [0]*len(arr)

        prefixMax[0] = arr[0] 

        #caculating prefixMax 
        for i in range(1,len(arr)) : 
            prefixMax[i] = max(prefixMax[i-1], arr[i])


        suffixMin[len(arr)-1] = arr[len(arr)-1]

        #calculating suffixMax
        for i in range(len(arr)-2 , -1 , -1) : 
            suffixMin[i] = min(suffixMin[i+1] , arr[i])

        
        for i in range(len(arr)-1) : 
            if prefixMax[i] <= suffixMin[i+1] : 
                count+=1
        
        return count+1