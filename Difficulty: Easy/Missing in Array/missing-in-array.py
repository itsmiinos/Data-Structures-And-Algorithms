class Solution:
    def missingNum(self, arr):
        # code here
        i = 0
        while i < len(arr) :
            while arr[i] < len(arr) and (arr[i] != i+1 and arr[i] != arr[arr[i]-1]) :
                arr[arr[i]-1] , arr[i] = arr[i] , arr[arr[i]-1]
            i+=1
        for i in range(len(arr)) :
            if arr[i] != i+1 :
                return i+1
        
        return len(arr)+1