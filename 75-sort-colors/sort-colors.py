class Solution:
    def sortColors(self, nums):
        i = 0
        j = 0
        k = len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
                # Don't move j here — check new value at nums[j] in next loop
            else:
                j += 1  # nums[j] == 1

        return nums
    
        