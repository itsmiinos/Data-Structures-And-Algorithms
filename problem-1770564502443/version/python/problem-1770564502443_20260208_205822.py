# Last updated: 2/8/2026, 8:58:22 PM
1class Solution:
2    def dominantIndices(self, nums: List[int]) -> int:
3        averageSuffix = [0]*len(nums)
4        averageSuffix[-1] = nums[-1]
5
6        sum = nums[-1]
7        count = 0
8        for i in range(len(nums)-2 , -1 , -1) :
9            average = sum / (len(nums) -  (i + 1))
10            # averageSuffix[i] = average
11            if average < nums[i] :
12                count+=1
13            sum = sum + nums[i]
14
15        # count = 0
16        # for i in range(len(nums)) :
17        #     if nums[i] > averageSuffix[i] :
18        #         count+=1
19
20        return count