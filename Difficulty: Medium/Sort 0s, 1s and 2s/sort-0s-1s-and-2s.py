class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        i = 0
        j = 0
        k = len(arr)-1
        
        while j <= k : 
            if arr[j] == 0 :
                [arr[i] , arr[j]] = [arr[j] , arr[i]]
                j+=1
                i+=1
            
            elif arr[j] == 1 : 
                j+=1
            
            elif arr[j] == 2 : 
                [arr[j] , arr[k]] = [arr[k] , arr[j]]
                k-=1