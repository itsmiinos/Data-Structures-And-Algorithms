class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.solve(nums , k) - self.solve(nums , k-1)
    
    def solve(self , nums , k) -> int :
        if k < 0 :
            return 0

        l = 0
        r = 0
        count_window_odd = 0
        count = 0

        while r < len(nums) :
            if nums[r]%2 != 0 :
                count_window_odd +=1
            
            while l <= r and count_window_odd > k :
                if nums[l]%2 != 0 :
                    count_window_odd -=1
                l+=1

            count += (r - l + 1)

            r+=1
        
        return count