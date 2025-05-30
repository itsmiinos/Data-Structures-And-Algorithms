class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        last_greater_element_index = 0
        previous_valid_starting_points = 0

        for ep in range(len(nums)) :
            if nums[ep] > right :
                last_greater_element_index = ep + 1
                previous_valid_starting_points = 0
            if nums[ep] >=left and nums[ep] <=right :
                ans += ep - last_greater_element_index + 1
                previous_valid_starting_points = ep - last_greater_element_index + 1
            if nums[ep] < left:
                ans += previous_valid_starting_points
            
        return ans