class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        i = 0
        j = 0
        count = 0
        max_len = 0
        while j < len(nums) :
            if nums[j] == 0 :
                while i <= j and count == 1:
                    if nums[i] == 0 :
                        count-=1
                    
                    i+=1
                count+=1
            if count <= 1 :
                max_len = max(max_len , j - i + 1)

            j+=1
        
        return max_len - 1
