# Last updated: 1/26/2026, 3:44:08 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        left = 0
4        seen = set()
5
6        for right in range(len(nums)):
7            if right - left > k:
8                seen.remove(nums[left])
9                left += 1
10
11            if nums[right] in seen:
12                return True
13
14            seen.add(nums[right])
15
16        return False
17
18            
19
20