# Last updated: 8/13/2025, 8:15:50 PM
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)) : 
            ans = 0
            for j in range (i , len(nums)) : 
                ans = self.gcd(ans , nums[j])
                if ans < k :
                    break
                if ans == k : 
                    count+=1
        return count
    
    def gcd(self , a : int , b : int) : 
        if a == 0 : 
            return b
        
        temp = self.gcd(b%a , a) 
        return temp