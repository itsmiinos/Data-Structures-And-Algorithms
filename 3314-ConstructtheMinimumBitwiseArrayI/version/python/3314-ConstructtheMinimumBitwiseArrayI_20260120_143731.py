# Last updated: 1/20/2026, 2:37:31 PM
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        result = []
4        for i in range(len(nums)) :
5            found = False
6            for j in range(1 , nums[i]) :
7                if (j | j+1) == nums[i] :
8                    found = True
9                    result.append(j)
10                    break
11            
12            if found == False : 
13                result.append(-1)
14        
15        return result