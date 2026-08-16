# Last updated: 8/16/2026, 9:47:57 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        my_map = collections.defaultdict(int)
4        sum = 0
5        count = 0
6        my_map[0] = 1
7
8        for i in range(len(nums)) :
9            sum+= nums[i]
10            diff = sum - k
11            if diff in my_map :
12                count += my_map[diff]
13           
14            my_map[sum] += 1
15        
16        return count