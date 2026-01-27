# Last updated: 1/28/2026, 12:11:24 AM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        left = 0
4        right = len(arr) - 1
5        
6        while right - left >= k:
7            if abs(x - arr[left]) > abs(x - arr[right]):
8                left += 1
9            else:
10                right -= 1
11        
12        return arr[left:right+1]