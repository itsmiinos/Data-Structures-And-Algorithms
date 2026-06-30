# Last updated: 6/30/2026, 10:36:54 PM
1class Solution:
2    def rearrangeArray(self, nums: List[int]) -> List[int]:
3        pos = 0
4        neg = 1
5        ans = [None]*len(nums)
6        i = 0
7        while i < len(nums) :
8            if nums[i] > 0 :
9                ans[pos] = nums[i]
10                pos+=2
11            else :
12                ans[neg] = nums[i]
13                neg+=2
14            i+=1
15        
16        return ans