# Last updated: 8/20/2026, 10:07:57 PM
1class Solution:
2    def resultArray(self, nums: List[int]) -> List[int]:
3        if len(nums) <= 2 :
4            return nums
5
6        arr1 = [nums[0]]
7        arr2 = [nums[1]]
8        i = 2
9        j = 0
10        k = 0
11
12        while i < len(nums) :
13            if arr1[j] > arr2[k] :
14                arr1.append(nums[i])
15                j+=1
16            else :
17                arr2.append(nums[i])
18                k+=1
19            
20            i+=1
21        
22        return arr1 + arr2