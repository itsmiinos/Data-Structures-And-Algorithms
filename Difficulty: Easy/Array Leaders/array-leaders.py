class Solution:
    def leaders(self, arr):
        # code here
        suffix_array = [0]* len(arr)
        suffix_array[-1] = arr[-1]
        
        for i in range(len(arr)-2 , -1 , -1) :
            if arr[i] > suffix_array[i+1] :
                suffix_array[i] = arr[i]
            else :
                suffix_array[i] = suffix_array[i+1]
        ans = []
        for i in range(len(suffix_array)) :
            if suffix_array[i] == arr[i] :
                ans.append(arr[i])
        
        return ans