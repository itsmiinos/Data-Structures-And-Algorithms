# Last updated: 2/8/2026, 9:41:32 PM
1heapq
2class Solution:
3    def countSubarrays(self, nums: List[int], k: int) -> int:
4        left = 0
5        right = 0
6        max_queue = []
7        min_queue = []
8        count = 0
9        
10        while right < len(nums) :
11            while len(max_queue) > 0 and nums[max_queue[-1]] < nums[right] :
12                max_queue.pop(-1)
13            max_queue.append(right)
14
15            while len(min_queue) > 0 and nums[min_queue[-1]] > nums[right] :
16                min_queue.pop(-1)
17            min_queue.append(right)
18            
19            while (nums[max_queue[0]] - nums[min_queue[0]]) * (right - left + 1) > k :
20                if max_queue[0] == left :
21                    max_queue.pop(0)
22
23                if min_queue[0] == left :
24                    min_queue.pop(0)
25
26                left+=1
27
28            if (nums[max_queue[0]] - nums[min_queue[0]]) * (right - left + 1) <= k :
29                count += right - left + 1
30
31            right+=1
32
33        return count