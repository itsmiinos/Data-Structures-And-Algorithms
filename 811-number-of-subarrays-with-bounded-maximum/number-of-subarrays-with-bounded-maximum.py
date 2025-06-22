class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        last_greater_element_index = 0 
        previous_valid_starting_points = 0 
        total_subarray_count = 0 

        n = len(nums)

        for i in range(n) : 
            if nums[i] > right : 
                last_greater_element_index = i+1
                previous_valid_starting_points = 0
            
            if nums[i] < left : 
                total_subarray_count += previous_valid_starting_points
            
            if nums[i] >= left and nums[i] <= right : 
                total_subarray_count += i - last_greater_element_index + 1
                previous_valid_starting_points = i - last_greater_element_index + 1
            
        return total_subarray_count