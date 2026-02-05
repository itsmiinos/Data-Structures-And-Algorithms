# Last updated: 2/5/2026, 1:31:36 PM
1class Solution:
2    def constructTransformedArray(self, nums: List[int]) -> List[int]:
3        result = [0]*len(nums)
4
5        for i in range(len(nums)) :
6            val = nums[i]
7            if val > 0 :
8                ind = i
9                while val > 0 :
10                    ind = (ind + 1) % len(nums)
11                    val-=1
12                result[i] = nums[ind]
13            elif val < 0 :
14                ind = i
15                val = abs(val)
16                while val > 0 :
17                    ind = ((ind - 1) + len(nums)) % len(nums)
18                    val-=1
19                result[i] = nums[ind]
20            else :
21                result[i] = nums[i]
22        
23        return result
24            