# Last updated: 2/3/2026, 2:06:50 AM
1class Solution:
2    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
3        return self.solve(nums , k) - self.solve(nums , k-1)
4    
5    def solve(self , nums : list , k : int) -> int :
6        right = 0
7        left = 0
8        count =0
9        numbers = collections.defaultdict(int)
10
11        while right < len(nums) :
12            numbers[nums[right]] +=1
13
14            while len(numbers) > k :
15                numbers[nums[left]] -=1
16                if numbers[nums[left]] == 0 :
17                    del numbers[nums[left]]
18                
19                left+=1
20            
21            count += right - left + 1
22        
23            right +=1
24        
25        return count
26                    
27            
28