#User function Template for python3

class Solution:

    def isPossible(self, S):
        my_map = {}
        
        for i in range(len(S)) : 
            my_map[S[i]] = my_map.get(S[i] , 0) + 1
        
        count = 0   
        for value in my_map.values() : 
            if value % 2 != 0 : 
                count+=1
        
        if len(S)%2 == 0 : 
            if count > 0 : 
                return 0
            return 1
            
        else : 
            if count > 1 : 
                return 0
            return 1