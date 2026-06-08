# Last updated: 6/8/2026, 9:24:50 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        map = {}
4        
5        for i in range(len(nums)) :
6            diff = target - nums[i]
7            if diff in map :
8                return [map[diff] , i]
9            
10            map[nums[i]] = i
11        
12        return []