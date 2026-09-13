class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        max_count = 0

        while j < len(nums) :
            if nums[j] == 0 :
                while i < len(nums) and k == 0 :
                    if nums[i] == 0 :
                        k+=1
                    i+=1
                k-=1
            max_count = max(max_count,j-i+1)

            j+=1
                
            
        
        return max_count
