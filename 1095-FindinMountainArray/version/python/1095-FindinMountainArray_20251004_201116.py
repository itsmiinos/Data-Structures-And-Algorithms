# Last updated: 10/4/2025, 8:11:16 PM
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # Step 1: Find the peak index
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        peak = low

        # Step 2: Binary search on increasing part
        low, high = 0, peak
        while low <= high:
            mid = (low + high) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        # Step 3: Binary search on decreasing part
        low, high = peak + 1, n - 1
        while low <= high:
            mid = (low + high) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                high = mid - 1
            else:
                low = mid + 1

        return -1
