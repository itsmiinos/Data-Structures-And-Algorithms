# Last updated: 11/10/2025, 9:29:57 PM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)) : 
            if i > 0 and nums[i] == nums[i-1] : continue
            for j in range(i+1 , len(nums)) : 
                if j > i+1 and nums[j] == nums[j-1] : continue
                k = j+1
                l = len(nums)-1

                while k < l :

                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum < target : 
                        k+=1
                    elif sum > target : 
                        l-=1
                    else : 
                        ans.add((nums[i] , nums[j] , nums[k] , nums[l]))
                        k+=1
                        l-=1
                    
                        while k < l and nums[k] == nums[k-1] : k+=1
                        while l > k and nums[l] == nums[l+1] : l-=1
        
        return list(ans)