class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_ans = 0

        for i in range(len(nums)) : 
            xor_ans = xor_ans ^ nums[i]

        set_bit = 0

        for i in range(32) : 
            if self.checkBit(xor_ans , i) : 
                set_bit = i
                break

        set1 = 0
        set2 = 0

        for i in range(len(nums)) : 
            if self.checkBit(nums[i] , set_bit) : 
                set1 = set1^nums[i]
            else : 
                set2 = set2^nums[i]
        
        return [set1 , set2]

    def checkBit(self , n:int , i : int) : 
        if n & (1<<i) : 
            return True
        return False