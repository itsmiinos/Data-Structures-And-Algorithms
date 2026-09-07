class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        i = 0
        while i < len(nums) :
            while i > 0 and i < len(nums) and nums[i-1] == nums[i] :
                i+=1
            
            j = i+1
            k = len(nums)-1

            while j < k :
                total = nums[i] + nums[j] + nums[k]

                if total > 0 :
                    k-=1
                elif total < 0 :
                    j+=1
                
                elif total == 0 :
                    ans.append([nums[i] , nums[j] , nums[k]])

                    j+=1
                    k-=1
                
                
                    while j < len(nums) and nums[j-1] == nums[j] :
                        j+=1
                        
                    while k > -1 and nums[k+1] == nums[k] :
                        k-=1
            
            i+=1
            
        return ans
            