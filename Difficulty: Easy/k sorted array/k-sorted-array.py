#User function Template for python3
import heapq
class Solution:
    def isKSortedArray(self, arr, n, k): 
        #code here.
        heap = []
        after_heaping = []
        
        for i in range(len(arr)) : 
            heapq.heappush(heap , (arr[i] , i))
        
        while len(heap) > 0 :
            after_heaping.append(heapq.heappop(heap))
        
        for i in range(len(after_heaping)) : 
            diff_in_index = abs(after_heaping[i][1] - i )
            # print(diff_in_index , after_heaping[i][0] ,after_heaping[i][1])
            if diff_in_index > k : 
                return "No"
        
        return "Yes"

class Pair : 
    def __init__(self , value : int , index : int) : 
        self.val = value
        self.index = index