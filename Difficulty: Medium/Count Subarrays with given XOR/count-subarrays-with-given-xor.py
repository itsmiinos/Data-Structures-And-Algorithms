from collections import defaultdict

class Solution:
    def subarrayXor(self, arr, k):
        freq = defaultdict(int)
        freq[0] = 1

        cummXor = 0
        count = 0

        for num in arr:
            cummXor ^= num
            diff = cummXor ^ k

            if diff in freq:
                count += freq[diff]

            freq[cummXor] += 1

        return count