class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        sum = 0
        last_greater_element = 0 
        previous_starting_points = 0

        for i in range (len(nums)) : 

            if nums[i] < left : 
                sum += previous_starting_points
            if nums[i] > right : 
                last_greater_element = i+1
                previous_starting_points = 0
            if nums[i] >=left and nums[i] <=right :
                previous_starting_points = i - last_greater_element + 1
                sum += i - last_greater_element + 1

        return sum