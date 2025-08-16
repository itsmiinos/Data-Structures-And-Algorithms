# Last updated: 8/16/2025, 4:26:53 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        arr = []
        temp = num
        
        while temp > 0 : 
            arr.append(temp%10)
            temp = temp//10

        for i in range(len(arr)-1 , -1 , -1) : 
            if arr[i] == 6 : 
                arr[i] =  9
                break
        
        ans = 0
        for i in range(len(arr)-1 , -1 , -1) : 
            ans = ans * 10 + arr[i]
        
        return ans