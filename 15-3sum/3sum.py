class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-1) :
            if i > 0 and nums[i-1] == nums[i] :
                continue
                 
            j = i+1
            k = len(nums)-1

            while j < k :
                summation = nums[i] + nums[j] + nums[k]

                if summation > 0 :
                    k-=1
                elif summation < 0 :
                    j+=1
                elif summation == 0 :
                    ans.append([nums[i] , nums[j] , nums[k]])

                    j+=1
                    k-=1
                
                    while j < len(nums) and nums[j] == nums[j-1] :
                        j+=1
                    
                    while k >= 0 and nums[k] == nums[k+1] :
                        k-=1
        
        return ans