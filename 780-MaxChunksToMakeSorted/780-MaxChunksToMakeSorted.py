# Last updated: 8/13/2025, 8:18:59 PM
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        prefixMax = [None]*len(arr)

        prefixMax[0] = arr[0]
        for i in range (1 , len(arr)) : 
            prefixMax[i] = max(prefixMax[i-1] , arr[i])

        count = 0
        for i in range(len(arr)) : 
            if prefixMax[i] == i : 
                count+=1
        
        return count