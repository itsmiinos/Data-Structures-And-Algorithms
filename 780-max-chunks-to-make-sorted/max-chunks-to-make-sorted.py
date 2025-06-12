import sys
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        max_value = -sys.maxsize

        for i in range(len(arr)) : 
            max_value = max(max_value , arr[i])

            if max_value == i : 
                count +=1
        
        return count