class Solution:
    def maxLength(self, arr):
        pSum = 0
        prefix_index = {}
        max_len = 0

        prefix_index[0] = -1  # base case

        for i in range(len(arr)):
            pSum += arr[i]

            if pSum in prefix_index:
                max_len = max(max_len, i - prefix_index[pSum])
            else:
                prefix_index[pSum] = i

        return max_len