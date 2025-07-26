#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        n1 = len(a)
        n2 = len(b)
        
        if n1 < n2 : 
            return self.kthElement(b , a , k)
        
        low = max(k-n2 , 0)
        high = min(k , n1)
        left = k
        
        while low <= high : 
            mid1 = low + (high - low) // 2
            mid2 = left - mid1
            
            l1 = a[mid1-1] if mid1 - 1 >= 0  else  float('-inf')
            l2 = b[mid2 - 1] if mid2 - 1 >= 0  else  float('-inf')
            r1 = a[mid1] if mid1 < n1 else float('inf')
            r2 = b[mid2] if mid2 < n2 else float('inf')
            
            if l1 <= r2 and l2 <= r1 : 
                return max(l1 , l2)
            
            elif l1 > r2 : high = mid1 - 1
            else : low = mid1 + 1
            
        return 0
