# Last updated: 1/19/2026, 8:13:06 PM
1from collections import defaultdict
2class Solution:
3    def subarraySum(self, nums: List[int], k: int) -> int:
4        map = defaultdict(int)
5        map[0] = 1
6        pSum = 0
7        count = 0
8        for i in range(len(nums)) :
9            pSum += nums[i]
10            diff = pSum - k
11            if diff in map :
12                count +=map[diff]
13            
14            map[pSum] +=1
15        
16
17        return count