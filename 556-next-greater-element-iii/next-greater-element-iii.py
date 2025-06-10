class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(d) for d in str(n)]
        dip_index = -1

        # Step 1: Find dip
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                dip_index = i - 1
                break

        if dip_index == -1:
            return -1  # No next permutation

        # Step 2: Find just greater element to the right of dip
        for i in range(len(nums) - 1, dip_index, -1):
            if nums[i] > nums[dip_index]:
                nums[i], nums[dip_index] = nums[dip_index], nums[i]
                break

        # Step 3: Reverse the suffix
        left = dip_index + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Step 4: Convert back to number and check limit
        number = int(''.join(map(str, nums)))
        return number if number < 2**31 else -1
