# Last updated: 7/31/2026, 10:44:13 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        i = 0
7        j = 0
8
9        # 1 , 5 , 6 , 0 , 0 , 0
10        # 4 , 2 , 3
11
12        while i < m and j < n :
13            if nums1[i] > nums2[j] :
14                nums1[i] , nums2[j] = nums2[j] , nums1[i]
15                k = j+1
16                while k < len(nums2) and nums2[k] < nums2[k-1] :
17                    nums2[k] , nums2[k-1] = nums2[k-1] , nums2[k]
18                    k+=1
19            i+=1
20        
21        while j < n :
22            nums1[i] = nums2[j]
23            i+=1
24            j+=1
25        
26        return nums1
27