class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.solve(nums , k) - self.solve(nums , k-1)


    def solve(self , nums : list , k : int) -> int :
        if k < 0 :
            return 0
        my_chars = collections.defaultdict(int)
        l = 0
        r = 0
        count = 0
        
        while r < len(nums) :
            my_chars[nums[r]] +=1
            
            while l<=r and len(my_chars) > k :
                my_chars[nums[l]] -=1
                if my_chars[nums[l]] == 0:
                    del my_chars[nums[l]]
                
                l+=1
            
            count+= (r - l + 1)
            
            r+=1
        
        return count