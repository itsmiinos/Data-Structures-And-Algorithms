# Last updated: 1/4/2026, 2:31:46 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        low = 0
4        high = len(nums) - 1
5
6        while low <= high :
7            
8            mid = low + ((high - low) // 2)
9
10            if nums[mid] == target : 
11                return mid
12            
13            elif nums[mid] <= nums[high] : 
14                if target <= nums[high] and nums[mid] < target : 
15                    low = mid + 1
16                else : 
17                    high = mid - 1   
18
19            elif nums[mid] > nums[high] : 
20                if target >= nums[low] and nums[mid] > target : 
21                    high = mid - 1
22                else : 
23                    low = mid + 1 
24        
25        return -1
26