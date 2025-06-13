#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        # Your code goes here
        count = 0
        for i in range (n) : 
            if a[i] == 0 : 
                a[i] = 1
            else : 
                a[i] = -1
                count+=1
        
        sum = 0 
        max_sum = 0
        
        for i in range(n) : 
            if sum<0 : 
                sum = a[i]
            else : 
                sum = sum + a[i]
                
            max_sum = max(sum , max_sum)
        
        if max_sum > 0 : 
            return max_sum + count
        else : 
            return count