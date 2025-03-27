class Solution(object):
    def sortColors(self, nums):
        i = 0
        j = 0
        k = len(nums)-1
        while j<=k :
            if nums[j] == 0 :
                [nums[i] , nums[j]] = [nums[j] , nums[i]]
                i+=1
                j+=1
            elif nums[j] == 2 :
                [nums[k] , nums[j]] = [nums[j] , nums[k]]
                k-=1
            elif nums[i] == 1 :
                [nums[i] , nums[j]] = [nums[j] , nums[i]]
                j+=1
        return nums
                
        