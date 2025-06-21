class Solution:
    def findSubarray(self, arr):
        prefixSum = 0
        count = 0
        map = {0: 1}  # Include zero prefix sum to handle cases where subarray from index 0 sums to 0

        for num in arr:
            prefixSum += num
            count += map.get(prefixSum, 0)
            map[prefixSum] = map.get(prefixSum, 0) + 1

        return count