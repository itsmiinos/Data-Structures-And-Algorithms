# Last updated: 2/8/2026, 8:57:53 PM
1class Solution:
2    def dominantIndices(self, nums: List[int]) -> int:
3        averageSuffix = [0]*len(nums)
4        averageSuffix[-1] = nums[-1]
5
6        sum = nums[-1]
7        for i in range(len(nums)-2 , -1 , -1) :
8            average = sum / (len(nums) -  (i + 1))
9            averageSuffix[i] = average
10            sum = sum + nums[i]
11
12        count = 0
13        for i in range(len(nums)) :
14            if nums[i] > averageSuffix[i] :
15                count+=1
16
17        return count