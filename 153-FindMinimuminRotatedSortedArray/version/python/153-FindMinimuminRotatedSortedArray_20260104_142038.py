# Last updated: 1/4/2026, 2:20:38 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        low = 0
4        high = len(nums)-1
5        ans = float('inf')
6        while low <= high :
7            mid = low + (high - low) // 2
8
9            if nums[mid] <= nums[high] :
10                ans = min(ans , nums[mid])
11                high = mid - 1
12            
13            else : 
14                low = mid + 1
15        
16        return ans