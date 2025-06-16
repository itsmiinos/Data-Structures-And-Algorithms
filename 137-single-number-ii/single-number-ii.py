class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32) : 
            count = 0
            for j in range(len(nums)) : 
                if self.checkBit(nums[j] , i) : 
                    count +=1
                
            if count%3 != 0 : 
                ans = ans + (1<<i) 

        if ans >= 2**31:
            ans -= 2**32

        return ans

    def checkBit(self , n : int , i : int) -> bool : 
        if n & (1<<i) : 
            return True
        return False