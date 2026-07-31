# Last updated: 7/31/2026, 10:52:43 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        productPrefix = []
4        productPrefix.append(nums[0])
5
6        for i in range(1 , len(nums)) : 
7            productPrefix.append(productPrefix[i-1] * nums[i])
8
9        
10        
11        product = 1
12
13        for i in range(len(nums)-1 , 0 , -1) :
14            productPrefix[i] = product * productPrefix[i-1]
15            product = nums[i] * product
16        
17        productPrefix[0] = product
18
19        return productPrefix