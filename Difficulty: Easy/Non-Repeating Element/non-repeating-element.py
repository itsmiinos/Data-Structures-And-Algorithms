#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        map = {}
        
        for i in range (len(arr)) : 
            map[arr[i]] = map.get(arr[i] , 0) + 1
        
        for key in map : 
            if map.get(key) == 1 : 
                return key
        
        return 0