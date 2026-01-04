# Last updated: 1/4/2026, 8:08:30 PM
1import math
2class Solution:
3    def sumFourDivisors(self, nums: List[int]) -> int:
4        ans = 0
5        divisors = {}
6
7        for i in range(len(nums)) :
8            if nums[i] in divisors :
9                if len(divisors[nums[i]]) == 4 : 
10                    ans += sum(divisors[nums[i]])
11            else :
12                divisors[nums[i]] = set()
13                for k in range(1 , int(sqrt(nums[i]))+1) :
14                    if nums[i] % k == 0 : 
15                        divisors[nums[i]].add(k)
16                        divisors[nums[i]].add(nums[i]//k)
17                if len(divisors[nums[i]]) == 4 : 
18                    ans+= sum(divisors[nums[i]])
19        
20        print(divisors)
21        return ans