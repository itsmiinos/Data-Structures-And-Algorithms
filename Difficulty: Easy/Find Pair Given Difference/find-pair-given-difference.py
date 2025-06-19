
from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        arr.sort()  # ✅ sort the array
        i = 0
        j = 1
        
        while j < len(arr):
            diff = arr[j] - arr[i]

            if i == j:  # Avoid comparing the same element
                j += 1
                continue

            if diff == x:
                return True
            elif diff < x:
                j += 1
            else:
                i += 1
        
        return False