class Solution:
    def largest(self, arr):
        # code here
        max = -1
        for i in range(len(arr)) :
            if arr[i] > max :
                max = arr[i]
                
        return max
