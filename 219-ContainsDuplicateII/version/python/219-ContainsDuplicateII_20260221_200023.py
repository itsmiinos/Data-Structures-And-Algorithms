# Last updated: 2/21/2026, 8:00:23 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        numbers = defaultdict(int)
4        left = 0
5        right = 0
6
7        while right < len(nums) :
8            if nums[right] in numbers :
9                return True
10            
11            numbers[nums[right]] +=1
12
13            if right - left + 1 > k :
14                numbers[nums[left]] -=1
15                if numbers[nums[left]] == 0 :
16                    del numbers[nums[left]]
17                left+=1
18            
19            right+=1
20        
21        return False