# Last updated: 8/13/2025, 8:24:47 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {} #val : index

        for i in range (0,len(nums)):
            diff = target - nums[i]

            if diff in my_dict :
                return [i , my_dict[diff]]
            else :
                my_dict[nums[i]] = i